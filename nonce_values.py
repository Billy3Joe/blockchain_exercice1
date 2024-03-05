package main

import (
	"crypto/rand"
	"crypto/sha256"
	"encoding/hex"
	"fmt"
	"math/big"
	"math/bits"
)

// calculateSHA256WithNonce calcule le haché SHA-256 d'un message avec un nonce donné.
func calculateSHA256WithNonce(message string, nonce *big.Int) string {
	messageWithNonce := fmt.Sprintf("%s%d", message, nonce)
	hash := sha256.Sum256([]byte(messageWithNonce))
	return hex.EncodeToString(hash[:])
}

// findNonce recherche un nonce produisant un haché avec les N bits de poids fort égaux à 0.
func findNonce(message string, leadingZeros int) *big.Int {
	nonce := new(big.Int)
	maxNonce := new(big.Int).Lsh(big.NewInt(1), 64) // Max nonce value (2^64)
	for {
		nonce, _ = rand.Int(rand.Reader, maxNonce)
		hashResult := calculateSHA256WithNonce(message, nonce)
		if leadingZeros == 0 || countLeadingZeros(hashResult) >= leadingZeros {
			return nonce
		}
	}
}

// countLeadingZeros compte le nombre de zéros de poids fort dans une chaîne hexadécimale.
func countLeadingZeros(hexString string) int {
	count := 0
	for _, c := range hexString {
		if c != '0' {
			break
		}
		count += 4 // 1 caractère hexadécimal = 4 bits
	}
	return count
}

// calculateStandardDeviation calcule l'écart-type d'un ensemble de valeurs.
func calculateStandardDeviation(values []*big.Int) float64 {
	if len(values) == 0 {
		return 0.0
	}
	var sum int64
	for _, v := range values {
		sum += v.Int64()
	}
	mean := float64(sum) / float64(len(values))
	var squaredDiffSum float64
	for _, v := range values {
		diff := float64(v.Int64()) - mean
		squaredDiffSum += diff * diff
	}
	variance := squaredDiffSum / float64(len(values))
	return float64(bits.Len64(uint64(len(values)))) * (variance / float64(len(values)))
}

func main() {
	// Tableau pour stocker les messages pour chaque valeur de N
	messages := make(map[int][]string)
	nonces := make(map[int][]*big.Int)

	// Générer 10 messages aléatoires pour chaque valeur de N
	for _, leadingZeros := range []int{4, 8, 12} {
		var messageList []string
		var nonceList []*big.Int
		for i := 0; i < 10; i++ {
			message := generateRandomMessage()
			messageList = append(messageList, message)
			nonce := findNonce(message, leadingZeros)
			nonceList = append(nonceList, nonce)
		}
		messages[leadingZeros] = messageList
		nonces[leadingZeros] = nonceList
	}

	// Afficher les messages et les nonces générés
	for leadingZeros, messageList := range messages {
		fmt.Printf("N=%d:\n", leadingZeros)
		for i, message := range messageList {
			fmt.Printf("Message %d: %s\n", i+1, message)
			fmt.Printf("Nonce: %d\n", nonces[leadingZeros][i])
			fmt.Println()
		}
	}

	// Afficher les statistiques pour chaque valeur de N
	for leadingZeros, nonceList := range nonces {
		fmt.Printf("N=%d:\n", leadingZeros)
		fmt.Printf("Number of nonces: %d\n", len(nonceList))
		if len(nonceList) > 0 {
			var sum int64
			for _, nonce := range nonceList {
				sum += nonce.Int64()
			}
			average := float64(sum) / float64(len(nonceList))
			fmt.Printf("Average nonce: %.2f\n", average)
			standardDeviation := calculateStandardDeviation(nonceList)
			fmt.Printf("Standard deviation of nonce: %.2f\n", standardDeviation)
		}
		fmt.Println()
	}
}

// generateRandomMessage génère un message aléatoire.
func generateRandomMessage() string {
	message := make([]byte, 16)
	rand.Read(message)
	return hex.EncodeToString(message)
}
