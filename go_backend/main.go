package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"sync"
	"time"
)

type Pet struct {
	Name     string `json:"name"`
	Type     string `json:"type"`
	Hunger   int    `json:"hunger"`
	Lifespan int    `json:"lifespan"`
}

var pets []Pet
var mu sync.Mutex

func applyHandler(w http.ResponseWriter, r *http.Request) {
	var data map[string][]Pet
	json.NewDecoder(r.Body).Decode(&data)

	mu.Lock()
	pets = data["pets"]
	mu.Unlock()

	fmt.Println("Applied pets:", pets)
	json.NewEncoder(w).Encode(map[string]string{"status": "zoo created"})
}

func destroyHandler(w http.ResponseWriter, r *http.Request) {
	mu.Lock()
	pets = nil
	mu.Unlock()

	fmt.Println("Zoo destroyed")
	json.NewEncoder(w).Encode(map[string]string{"status": "zoo destroyed"})
}

func statusHandler(w http.ResponseWriter, r *http.Request) {
	mu.Lock()
	defer mu.Unlock()

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(pets)
}

func feedHandler(w http.ResponseWriter, r *http.Request) {
	mu.Lock()
	defer mu.Unlock()

	for i := range pets {
		if pets[i].Hunger > 0 {
			pets[i].Hunger -= 1
		}
	}

	fmt.Println("🍖 All pets have been fed.")
	json.NewEncoder(w).Encode(map[string]string{"status": "pets fed"})
}

// --- Pet Simulation Goroutine ---
func startPetLifeCycle() {
	ticker := time.NewTicker(5 * time.Second)

	for {
		<-ticker.C
		mu.Lock()

		for i := 0; i < len(pets); {
			pets[i].Hunger += 1
			pets[i].Lifespan -= 1

			if pets[i].Lifespan <= 0 {
				fmt.Printf("💀 %s the %s has passed away.\n", pets[i].Name, pets[i].Type)
				// Remove dead pet
				pets = append(pets[:i], pets[i+1:]...)
			} else {
				i++ // only increment if not removed
			}
		}

		mu.Unlock()
	}
}

func main() {
	go startPetLifeCycle()

	http.HandleFunc("/apply", applyHandler)
	http.HandleFunc("/destroy", destroyHandler)
	http.HandleFunc("/status", statusHandler)
	http.HandleFunc("/feed", feedHandler)

	fmt.Println("Server listening on :8080")
	http.ListenAndServe(":8080", nil)
}
