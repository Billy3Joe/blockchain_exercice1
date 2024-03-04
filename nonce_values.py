import hashlib
import secrets
import statistics

def calculate_sha256(message):
    """
    Calcule le haché SHA-256 d'un message.
    """
    return hashlib.sha256(message.encode()).hexdigest()

def calculate_sha256_with_nonce(message, nonce):
    """
    Calcule le haché SHA-256 d'un message avec un nonce donné.
    """
    message_with_nonce = f"{message}{nonce}"
    return hashlib.sha256(message_with_nonce.encode()).hexdigest()

def find_nonce(message, leading_zeros):
    """
    Recherche un nonce produisant un haché avec les N bits de poids fort égaux à 0.
    """
    nonce_length = 32  # Longueur du nonce en bytes
    while True:
        nonce = secrets.token_bytes(nonce_length)  # Générer un nonce aléatoire
        hash_result = calculate_sha256_with_nonce(message, nonce)
        if hash_result.startswith('0' * leading_zeros):
            return int.from_bytes(nonce, 'big')  # Convertir le nonce hexadécimal en entier pour N=4 et N=12

def execute_find_nonce(message, leading_zeros, attempts=10):
    """
    Exécute la recherche de nonce plusieurs fois et établit des statistiques.
    """
    nonce_values = []
    for _ in range(attempts):
        nonce = find_nonce(message, leading_zeros)
        if nonce is not None:
            nonce_values.append(nonce)
    return nonce_values

# Message à utiliser
message = "Hello, world!"

# Dictionnaire pour stocker les nonces pour chaque valeur de N
nonce_statistics = {}

# Exécution pour N=4, 8 et 12
for leading_zeros in [4, 8, 12]:
    nonce_values = execute_find_nonce(message, leading_zeros, attempts=10)
    nonce_statistics[leading_zeros] = nonce_values
    print(f"N={leading_zeros}:")
    print("Nonce values:", nonce_values)
    print("Number of nonces:", len(nonce_values))
    print("Average nonce:", statistics.mean(nonce_values))
    print("Standard deviation of nonce:", statistics.stdev(nonce_values))
    print("")

# Affichage des statistiques globales
print("Overall statistics:")
for leading_zeros, nonce_values in nonce_statistics.items():
    print(f"N={leading_zeros}:")
    print("Number of nonces:", len(nonce_values))
    print("Average nonce:", statistics.mean(nonce_values))
    print("Standard deviation of nonce:", statistics.stdev(nonce_values))
    print("")
