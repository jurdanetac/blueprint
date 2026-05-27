// Output: "May 24, 2026 at 17:51"
const timeFormatter = new Intl.DateTimeFormat('en-US', {
  dateStyle: 'medium',
  timeStyle: 'short',
  hour12: false
});

// Get live clock element
const liveClockElement = document.getElementById("live-clock");

function updateLiveClock() {
  // Get now's timestamp
  const now = new Date();

  // Set it to the clock element as text
  liveClockElement.textContent = `It is ${timeFormatter.format(now)}`;
  liveClockElement.setAttribute("datetime", now.toISOString());
};

// Update it immediately since it's empty by default
updateLiveClock();

// Update live clock every second
setInterval(updateLiveClock, 1000);
