// Populate available voices
function populateVoices() {
    console.log('Available voices:', window.speechSynthesis.getVoices());
}

// Call populateVoices when the voices have loaded (only once)
if (window.speechSynthesis.onvoiceschanged !== undefined) {
    window.speechSynthesis.onvoiceschanged = populateVoices;
} else {
    populateVoices();
}

// Function to speak the story text
function speakStory() {
    const storyText = document.getElementById("story-text").innerText;
    const utterance = new SpeechSynthesisUtterance(storyText);

    // Set language
    utterance.lang = "en-US";

    // Speak the text
    window.speechSynthesis.speak(utterance);
}

// Function to pause the speech
function pauseStory() {
    if (window.speechSynthesis.speaking && !window.speechSynthesis.paused) {
        window.speechSynthesis.pause();
        console.log("Speech paused");
    }
}

// Function to resume the speech
function resumeStory() {
    if (window.speechSynthesis.paused) {
        window.speechSynthesis.resume();
        console.log("Speech resumed");
    }
}

// Function to stop the speech
function stopStory() {
    if (window.speechSynthesis.speaking) {
        window.speechSynthesis.cancel();
        console.log("Speech stopped");
    }
}
