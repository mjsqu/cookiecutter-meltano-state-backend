"""A state store manager that uses {{ cookiecutter.backend }} as the backend."""

from __future__ import annotations

import typing as t

from meltano.core.job_state import JobState
from meltano.core.setting_definition import SettingDefinition
from meltano.core.state_store.base import StateStoreManager

#TODO: Insert import statements for dependent modules that allow you to connect 
#      to your custom backend

class {{ cookiecutter.backend }}StateStoreManager(StateStoreManager):  # type: ignore[misc]
    """A state store manager that uses {{ cookiecutter.backend }} as the backend."""

    label: str = "{{ cookiecutter.backend }}"

    def __init__(
        self,
        uri: str,
        *,
        # TODO: Add parameters as required
        **kwargs: t.Any,
    ) -> None:
        """Create a {{ cookiecutter.backend }}StateStoreManager.

        Args:
            uri: The URI to use to connect to the {{ cookiecutter.backend }} database
            **kwargs: Additional kwargs to pass to the underlying rocksdict.Rdict
        """
        super().__init__(**kwargs)
        self.uri = uri
        self.scheme, self.path = uri.split("://", 1)

        # TODO: Process any extra parameters and setup a connection to your backend

    def set(self, state: JobState) -> None:
        """Set state for the given state_id.

        Args:
            state: The state to set
        """
        if state.is_complete():
            state_payload = {
                "completed": state.completed_state,
                "partial": state.partial_state,
            }
        
        else:
            existing_state: dict[str, t.Any] = self._get(state.state_id)  # type: ignore[assignment]
            if existing_state:
                state_to_write = JobState(
                    state_id=state.state_id,
                    completed_state=existing_state.get("completed", {}),
                    partial_state=existing_state.get("partial", {}),
                )
                state_to_write.merge_partial(state)
            else:
                state_to_write = state

            state_payload = {
                "completed": state_to_write.completed_state,
                "partial": state_to_write.partial_state,
            }

        # TODO: Code to store the state_payload value into your backend

        return

    def _get(self, state_id: str) -> dict[str, t.Any] | None:
        """Internal get function for {{ cookiecutter.backend }}.

        Args:
            state_id: The state_id to get state for
        Returns:
            Dict representing state that would be used in the next run.
        """
        
        # TODO: Write the logic to return state as a dict from your backend
        state_dict = {}
        
        return state_dict


    def get(self, state_id: str) -> JobState | None:
        """Get state for the given state_id.
        Args:
            state_id: The state_id to get state for
        Returns:
            Dict representing state that would be used in the next run.
        """
        state_dict: dict[str, t.Any] | None = self._get(state_id)
        return (
            JobState(
                state_id=state_id,
                completed_state=state_dict.get("completed", {}),
                partial_state=state_dict.get("partial", {}),
            )
            if state_dict
            else None
        )

    def clear(self, state_id: str) -> None:
        """Clear state for the given state_id.
        Args:
            state_id: the state_id to clear state for
        """
        # TODO: Add delete logic

    def get_state_ids(self, pattern: str | None = None) -> list[str]:
        """Get all state_ids available in this state store manager.
        Args:
            pattern: glob-style pattern to filter by
        Returns:
            List of state_ids available in this state store manager.
        """
        # TODO: Write a function to retrieve all state IDs from your backend
        state_ids = []

        return state_ids

    def acquire_lock(self, state_id: str) -> None:
        """Acquire a naive lock for the given job's state.
        Args:
            state_id: the state_id to lock
        """
        pass  # pragma: no cover