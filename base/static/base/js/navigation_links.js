const activeLinkClassName = "text-blue-400";
const inactiveLinkClassName = "text-slate-400";
const navigationListUl = document.getElementById("navigation-list");

// Leverage event bubbling
navigationListUl.addEventListener("click", (event) => {
    const navigationAnchor = event.target.closest("a");

    // Clicked a li, not the anchor
    if (!navigationAnchor) return;
    // Already active
    if (navigationAnchor.classList.contains(activeLinkClassName)) return;

    // Turn off the previously active navigation anchor
    const previous = navigationListUl.querySelector("." + activeLinkClassName);
    previous.classList.replace(activeLinkClassName, inactiveLinkClassName);

    // Add the active class
    navigationAnchor.classList.replace(inactiveLinkClassName, activeLinkClassName);
});