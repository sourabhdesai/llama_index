class WorkflowValidationError(Exception):
    pass


class WorkflowTimeoutError(Exception):
    pass


class WorkflowRuntimeError(Exception):
    def get_original_cause(self) -> Exception | None:
        curr_exc = self.__cause__
        while isinstance(curr_exc, WorkflowRuntimeError):
            curr_exc = curr_exc.__cause__
        return curr_exc


class WorkflowDone(Exception):
    pass


class WorkflowCancelledByUser(Exception):
    pass


class WorkflowStepDoesNotExistError(Exception):
    pass


class WorkflowConfigurationError(Exception):
    pass
