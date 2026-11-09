class LoginService:
    """
    Coordinates login-related work without handling an HTTP request.
    """

    def login(self, username, password):
        """
        Checks the supplied credentials and identifies the account to log in.

        Parameters:
            username: the account name supplied by the user.
            password: the password supplied by the user.

        Preconditions:
            - username is a non-empty string.
            - password is a non-empty string.

        Postconditions:
            - Returns the account associated with valid credentials.
            - Does not change unrelated accounts.

        Side effects:
            - None specified until the login design is defined.

        Raises:
            NotImplementedError until the student implements the login logic.
        """
        raise NotImplementedError

    def logout(self, username):
        """
        Ends the login session for an account.

        Parameters:
            username: the account name whose session should end.

        Preconditions:
            - username is a non-empty string.

        Postconditions:
            - The account is no longer logged in.

        Side effects:
            - Ends the account's login session.

        Raises:
            NotImplementedError until the student implements the logout logic.
        """
        raise NotImplementedError

    def is_logged_in(self, username):
        """
        Checks whether an account has an active login session.

        Parameters:
            username: the account name to check.

        Preconditions:
            - username is a non-empty string.

        Postconditions:
            - Returns whether the account has an active login session.

        Side effects:
            - None.

        Raises:
            NotImplementedError until the student implements the session-checking logic.
        """
        raise NotImplementedError
