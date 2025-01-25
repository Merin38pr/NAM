
let voices = [];

// Populate available voices
function populateVoices() {
    voices = window.speechSynthesis.getVoices();
    console.log('Available voices:', voices);  // This will help debug the available voices
}

// Call populateVoices when the voices have loaded (only once)
window.speechSynthesis.onvoiceschanged = populateVoices;

// Function to speak the story text
function speakStory() {
    const storyText = document.getElementById("story-text").innerText;
    const utterance = new SpeechSynthesisUtterance(storyText);

    // Set language and select a voice
    utterance.lang = "en-US";

    // Wait until voices are loaded before selecting a voice
    if (voices.length === 0) {
        alert("No voices loaded yet. Please try again.");
        return;
    }

    // Example: Set the voice to a female voice (if available)
    const selectedVoice = voices.find(voice => voice.name === "Google UK English Female");

    if (selectedVoice) {
        utterance.voice = selectedVoice;
    } else {
        console.warn("The selected voice was not found. Falling back to default.");
    }

    // Speak the text
    window.speechSynthesis.speak(utterance);
}

// Function to pause the speech
function pauseStory() {
    if (window.speechSynthesis.speaking) {
        window.speechSynthesis.pause();
    }
}

// Function to resume the speech
function resumeStory() {
    if (window.speechSynthesis.paused) {
        window.speechSynthesis.resume();
    }
}
function stopStory() {
    window.speechSynthesis.cancel();  // Stops all speech
}
