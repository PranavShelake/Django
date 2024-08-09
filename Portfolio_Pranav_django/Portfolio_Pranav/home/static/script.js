const typingAnimationElement = document.getElementById('typing-animation');

// Create an array of typing text
const typingTexts = [' Web Developer', ' Machine Learning Engineer', ' Data Scientist', ' Competitive Programmer'];

// Function to display the typing animation for a given text
function playTypingAnimation(text, index = 0) {
  if (index < text.length) {
    typingAnimationElement.textContent += text[index];
    setTimeout(() => {
      playTypingAnimation(text, index + 1);
    }, 100); // Adjust delay for typing speed
  } else {
    setTimeout(() => {
      deleteTypingAnimation(text);
    }, 2000); // Delay before deleting starts
  }
}

// Function to display the deleting animation
function deleteTypingAnimation(text, index = text.length) {
  if (index > 0) {
    typingAnimationElement.textContent = text.slice(0, index - 1);
    setTimeout(() => {
      deleteTypingAnimation(text, index - 1);
    }, 100); // Adjust delay for deleting speed
  } else {
    setTimeout(() => {
      const nextIndex = (typingTexts.indexOf(text) + 1) % typingTexts.length;
      playTypingAnimation(typingTexts[nextIndex]);
    }, 500); // Delay before starting the next typing animation
  }
}

// Start the animation with the first text in the array
playTypingAnimation(typingTexts[0]);


function toggleDropdown(id, element) {
  // Prevent the event from bubbling up to the parent elements
  event.stopPropagation();

  var content = document.getElementById(id);
  var isOpen = content.style.display === "block";

  // Toggle visibility
  content.style.display = isOpen ? "none" : "block";

  // Change the icon
  var icon = element.querySelector('path');
  var currentPath = icon.getAttribute("d");

  // Define the paths for each icon state
  const plusPath = "M256 80c0-17.7-14.3-32-32-32s-32 14.3-32 32l0 144L48 224c-17.7 0-32 14.3-32 32s14.3 32 32 32l144 0 0 144c0 17.7 14.3 32 32 32s32-14.3 32-32l0-144 144 0c17.7 0 32-14.3 32-32s-14.3-32-32-32l-144 0 0-144z";
  const minusPath = "M432 256c0 17.7-14.3 32-32 32L48 288c-17.7 0-32-14.3-32-32s14.3-32 32-32l352 0c17.7 0 32 14.3 32 32z";
  const upArrowPath = "M201.4 137.4c12.5-12.5 32.8-12.5 45.3 0l160 160c12.5 12.5 12.5 32.8 0 45.3s-32.8 12.5-45.3 0L224 205.3 86.6 342.6c-12.5 12.5-32.8 12.5-45.3 0s-12.5-32.8 0-45.3l160-160z";
  const downArrowPath = "M201.4 374.6c12.5 12.5 32.8 12.5 45.3 0l160-160c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0L224 306.7 86.6 169.4c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3l160 160z";

  if (currentPath === plusPath) {
    // Toggle from plus to minus
    icon.setAttribute("d", minusPath);
  } else if (currentPath === minusPath) {
    // Toggle from minus to plus
    icon.setAttribute("d", plusPath);
  } else if (currentPath === upArrowPath) {
    // Toggle from up to down arrow
    icon.setAttribute("d", downArrowPath);
  } else if (currentPath === downArrowPath) {
    // Toggle from down to up arrow
    icon.setAttribute("d", upArrowPath);
  }
}

// M192 64C86 64 0 150 0 256S86 448 192 448l192 0c106 0 192-86 192-192s-86-192-192-192L192 64zm192 96a96 96 0 1 1 0 192 96 96 0 1 1 0-192z
// M384 128c70.7 0 128 57.3 128 128s-57.3 128-128 128l-192 0c-70.7 0-128-57.3-128-128s57.3-128 128-128l192 0zM576 256c0-106-86-192-192-192L192 64C86 64 0 150 0 256S86 448 192 448l192 0c106 0 192-86 192-192zM192 352a96 96 0 1 0 0-192 96 96 0 1 0 0 192z

function switchmode() {
  let switchmodeElement = document.querySelector("body");
  let button = document.querySelector("#button");
  let currentMode = switchmodeElement.getAttribute("class");

  if (currentMode === "night") {
    // Switch to day mode
    switchmodeElement.setAttribute("class", "day");
    
    button.querySelector('path').setAttribute("d", "M384 128c70.7 0 128 57.3 128 128s-57.3 128-128 128l-192 0c-70.7 0-128-57.3-128-128s57.3-128 128-128l192 0zM576 256c0-106-86-192-192-192L192 64C86 64 0 150 0 256S86 448 192 448l192 0c106 0 192-86 192-192zM192 352a96 96 0 1 0 0-192 96 96 0 1 0 0 192z");
    
  } else {
    // Switch to night mode
    switchmodeElement.setAttribute("class", "night");
    button.querySelector('path').setAttribute("d", "M192 64C86 64 0 150 0 256S86 448 192 448l192 0c106 0 192-86 192-192s-86-192-192-192L192 64zm192 96a96 96 0 1 1 0 192 96 96 0 1 1 0-192z");
  }
}
