class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password)<8:
            return False
        if not any(x.islower() for  x in password):
            return False
        if not any(x.isupper() for  x in password):
            return False
        if not any(x.isdigit() for  x in password):
            return False
        if not any(x  in "!@#$%^&*()-+" for  x in password):
            return False

        pre=None
        for c in password:
            if pre!=None and c==pre:
                return False
            pre=c

        return True

