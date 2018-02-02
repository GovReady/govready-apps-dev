/* iOS only activates :hover on elements that have click behavior.
   But more responsive is to use touchstart, rather than click, which
   activates :active. Here we add a function that makes everything
   touchable?? I'm not sure if we should restrict this just to the
   .comic-strip-frame elements, but this works. */
document.addEventListener("touchstart", function() {}, false);
