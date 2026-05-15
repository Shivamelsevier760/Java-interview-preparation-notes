# Existing code in the CDM for the checkmarx

```jsx
	private List<ChangeRequest> getChangeRequestDetailsForRequestor(String requestorName, String approverName,
																	String status) {

		if (status == null || !status.matches("Closed|Rejected|Approved")) {
			return changeRequestRepository.findChangeRequestDetails(requestorName, status, approverName);
		} else {
			return changeRequestRepository.findClosedChangeRequestDetailsForRequestor(requestorName);
		}
	}
```

```jsx
	@Override
	public List<String> searchRequestor(String requestorName) {
		return changeRequestRepository.findRequestorName(requestorName);
	}
```

```jsx
	@Test
	public void testGetRequestorNames() {
		List<String> listOfRequestorNames = new ArrayList<>();
		listOfRequestorNames.add("G, Arun karthikeyan");

		when(changeRequestService.searchRequestor(Mockito.anyString())).thenReturn(listOfRequestorNames);
		ResponseEntity<List<String>> response = changeRequestApiController.searchRequestor("arun");
		assertEquals(HttpStatus.OK, response.getStatusCode());
	}
```

```jsx
public ChangeRequestUpdateDTO getChangeRequestDetailsById(Long changeRequestId) {
		ChangeRequest changeRequest = changeRequestRepository.findById(changeRequestId)
				.orElseThrow(() -> new NotFoundException("Change request not avaialble " + changeRequestId));
		List<ChangeRequestActivity> changeRequestActivities = changeRequestActivityRepository
				.findbyChangeRequestId(changeRequestId);
		return changeRequestServiceHelper.getChangeRequestDetailsById(changeRequest, changeRequestActivities);
	}
```

```jsx

	@Test
	public void testAddGetChangeRequestDetailsById() {
		ChangeRequestUpdateDTO changeRequestUpdateDTO = buildValidchangeRequestUpdateDTO();

		when(changeRequestService.getChangeRequestDetailsById(Mockito.anyLong())).thenReturn(changeRequestUpdateDTO);
		ResponseEntity<ChangeRequestUpdateDTO> response = changeRequestApiController
				.getChangeRequest(Mockito.anyLong());
		assertEquals(HttpStatus.OK, response.getStatusCode());
	}
```

```jsx
private ChangeRequest getChangeRequest(Long id) {
		return changeRequestRepository.findById(id)
				.orElseThrow(() -> new NotFoundException("Change request not avaialble " + id));
	}
```

```jsx
	public List<RejectionReasonsDTO> getRejectionReasons() {
		List<RejectionReasonsDTO> rejectionReasonsDTOs = new ArrayList<>();
		RejectionReasonsDTO rejectionReasonsDTO = null;
		for (RejectionReason rejectionReason : rejectionReasonRepository.findAll()) {
			rejectionReasonsDTO = new RejectionReasonsDTO();
			BeanUtils.copyProperties(rejectionReason, rejectionReasonsDTO);
			rejectionReasonsDTOs.add(rejectionReasonsDTO);
		}
		return rejectionReasonsDTOs;

	}
```

```jsx
	@Test
	public void testGetRejectionReasonDetails() {
		List<RejectionReasonsDTO> rejectionReasonsDTOs = new ArrayList<>();

		rejectionReasonsDTO = buidRejectionReasonDTO();
		rejectionReasonsDTOs.add(rejectionReasonsDTO);
		when(rejectionReasonService.getRejectionReasons()).thenReturn(rejectionReasonsDTOs);
		ResponseEntity<List<RejectionReasonsDTO>> response = rejectionReasonsApiController.rejectionReasons();
		assertEquals(HttpStatus.OK, response.getStatusCode());
	}
```

```jsx
	private List<OrganizationAttribute> getOrganizationAttributes() {
		return organizationAttributeRepository.findAll();
	}
```

```jsx
	public List<OrganizationAttribute> getAllOrganizationAttributes() {
		return  organisationAttributeRepository.findAll();
	}
```

```jsx
	@Override
	public List<ClassificationDTO> getClassifications() {

		List<ClassificationDTO> classificationDTOs = new ArrayList<>();
		for (Classification classification : classificationRepository.findAll()) {
			ClassificationDTO classificationDTO = new ClassificationDTO();
			BeanUtils.copyProperties(classification, classificationDTO);
			classificationDTOs.add(classificationDTO);
		}
		return classificationDTOs;
	}
	
```

```jsx
	public List<ChangeReasonDTO> getChangeReasons() {
		List<ChangeReasonDTO> changeReasonDTOs = new ArrayList<>();
		ChangeReasonDTO changeReasonDTO = null;
		for (ChangeReason changeReason : changeReasonRepository.findAll()) {
			changeReasonDTO = new ChangeReasonDTO();
			BeanUtils.copyProperties(changeReason, changeReasonDTO);
			changeReasonDTOs.add(changeReasonDTO);
		}
		return changeReasonDTOs;
	}
```

```jsx
@Override
	@Transactional
	public AssignResponseDTO assignTo(List<AssignDTO> assignToDTO) {
		AssignResponseDTO assignResponseDTO = new AssignResponseDTO();
		for (AssignDTO assignDTO : assignToDTO) {
			ChangeRequest changeRequest = changeRequestRepository.findById(assignDTO.getChangeRequestId()).orElseThrow(
					() -> new NotFoundException("Change request not avaialble " + assignDTO.getChangeRequestId()));
			String asssignTo = checkAndRemoveParanthesis(assignDTO.getAssignTo());
			Map<String, Approver> approverMap = getApproverDetails();

			Approver approver = approverMap.get(asssignTo);
			if (approver != null) {
				changeRequest.setAssignedTo(assignDTO.getAssignTo());
				changeRequest.setStatus(getStatuses().get(ApplicationConstants.REQUEST_ASSIGNED));
				changeRequest.setCurrentApproverId(approver.getId());
				changeRequest.setRequestorStatus(ApplicationConstants.PENDING_APPROVAL_ECH_TEAM);
				changeRequest.setTicketStatus(ApplicationConstants.PENDING);
				changeRequestRepository.save(changeRequest);
				ChangeRequestActivity changeRequestActivity = new ChangeRequestActivity();
				changeRequestActivity.setApprovalLevelId(approver.getApprovalId());
				changeRequestActivity.setApproverId(approver.getId());
				changeRequestActivity.setActivityStatus(getStatuses().get(ApplicationConstants.REQUEST_ASSIGNED));
				changeRequestActivity.setRequestorStatus(ApplicationConstants.PENDING_APPROVAL_ECH_TEAM);
				changeRequestActivity.setTicketStatus(ApplicationConstants.PENDING);
				changeRequestActivity.setActivityDate(LocalDateTime.now());
				changeRequestActivity.setCreatedBy(asssignTo);
				changeRequestActivity.setLastModifiedBy(asssignTo);
				changeRequestActivity.setChangeRequest(changeRequest);
				changeRequestActivity.setCreatedDate(LocalDateTime.now());
				changeRequestActivity.setLastModifiedDate(LocalDateTime.now());
				changeRequest.setCurrentApproverId(approver.getId());
				changeRequestActivityRepository.save(changeRequestActivity);
			}

		}
		assignResponseDTO.setStatusCodeDescription("change request assigned successfully");
		return assignResponseDTO;

	}
```

```jsx
	@Override
	public ApproverDetailsDTO getApproverDetails(Long approverId) {
		if (approverId == null) {
			throw new NotFoundException("approverId  required to get the approver details ");
		}
		ApproverDetailsDTO approverDetailsDTO = null;
		Approver approver = approverRepository.findById(approverId)
				.orElseThrow(() -> new NotFoundException("Approver not found for the id " + approverId));
		approverDetailsDTO = new ApproverDetailsDTO();
		BeanUtils.copyProperties(approver, approverDetailsDTO);
		approverDetailsDTO.setApproverId(approver.getId());
		return approverDetailsDTO;
	}
```

```jsx
	@Test
	public void testGetApproverDtails() {
		ApproverDetailsDTO approverDetailsDTO = buildApproverDetailsDTO().get(0);

		Optional<Approver> approver = Optional.of(new Approver());
		approver.get().setId(1l);
		approver.get().setFirstName("Bob");
		approver.get().setLastName("Bob");

		when(approverRepository.findById(Mockito.anyLong())).thenReturn(approver);

		ApproverDetailsDTO actualApproverDetailsDTO = approverService.getApproverDetails(Mockito.anyLong());
		assertEquals(approverDetailsDTO.getFirstName(), actualApproverDetailsDTO.getFirstName());
	}
```

```jsx
	private Long getAccountPersonSequence() {
		return saAccountRepository.getAccountPersonSequence();
	}
```

```jsx
	private Long submitLoad(Long loadId) {
			return gdAccountRepository.submitLoad(loadId);
	}
```

```jsx
private Long getLoadId() {
		return gdAccountRepository.getLoadId();
	}
```

```jsx
	private Long isChangeRequestAvaialbeForPushToECH() {
		return changeRequestRepository.isChangeRequestsAvailableForPushToECH();
	}
```

```jsx
	private PatternStatusConfig getPatternStatusConfig(Long patternId) {
		PatternStatusConfigFactory patternStatusConfigFactory = new PatternStatusConfigFactory();
		Pattern pattern = patternRepository.findById(patternId)
				.orElseThrow(() -> new NotFoundException("Pattern not forund for the patternId " + patternId));
		return patternStatusConfigFactory.getPatternStatus(pattern.getPatternName());
	}
```

```jsx
	private Approver getApprover(Long approverId) {
		return approverRepository.findById(approverId)
				.orElseThrow(() -> new NotFoundException("Approver not forund for the approverId " + approverId));
	}
```

```jsx
	private Approval getApprovalDetailsById(Long approvalId) {
		return approvalRepository.findById(approvalId)
				.orElseThrow(() -> new NotFoundException("Approval not forund for the approvalId " + approvalId));
	}
```