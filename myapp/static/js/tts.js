function speakStory() {
    const storyText = document.getElementById("story-text").innerText;
    const utterance = new SpeechSynthesisUtterance(storyText);
    utterance.lang = "en-US";
    window.speechSynthesis.speak(utterance);
}
