class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs)==0:
            return 'None'
        encoded_str = '*'+"@123/./@".join(strs)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        if s=='None':
            return []
        decoded_str = s[1:].split('@123/./@')
        return decoded_str
