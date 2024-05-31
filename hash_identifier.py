import re

class HashIdentifier:
    def getData(self, hash):
        hash_patterns = {
            'MD5': r'^[a-f0-9]{32}$',
            'SHA-1': r'^[a-f0-9]{40}$',
            'SHA-224': r'^[a-f0-9]{56}$',
            'SHA-256': r'^[a-f0-9]{64}$',
            'SHA-384': r'^[a-f0-9]{96}$',
            'SHA-512': r'^[a-f0-9]{128}$',
            'SHA3-224': r'^[a-f0-9]{56}$',
            'SHA3-256': r'^[a-f0-9]{64}$',
            'SHA3-384': r'^[a-f0-9]{96}$',
            'SHA3-512': r'^[a-f0-9]{128}$',
            'NTLM': r'^[a-f0-9]{32}$',
            'MD4': r'^[a-f0-9]{32}$',
            'CRC32': r'^[a-f0-9]{8}$',
            'RIPEMD-160': r'^[a-f0-9]{40}$',
            'Whirlpool': r'^[a-f0-9]{128}$',
            'Blake2b': r'^[a-f0-9]{128}$',
            'Blake2s': r'^[a-f0-9]{64}$'
        }
        
        algorithms = []
        for algorithm, pattern in hash_patterns.items():
            if re.match(pattern, hash, re.IGNORECASE):
                algorithms.append(algorithm)
        
        if algorithms:
            return {"status": "success", "types": algorithms}
        return {"status": "failed", "types": "None"}

if __name__ == '__main__':
    hash_string = input("Enter a hash to be identified: ")
    hash_identifier = HashIdentifier()
    detected_algorithms = hash_identifier.getData(hash_string)
    if detected_algorithms["status"] == "success":
        print("Detected hash algorithms:", detected_algorithms["types"])
    else:
        print("No matching hash algorithm found.")
