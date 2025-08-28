
document.addEventListener('DOMContentLoaded', function(){
  // add small keyboard nav focus effect
  const links = document.querySelectorAll('.main-nav a');
  let idx = 0;
  document.addEventListener('keydown', (e) => {
    if(e.key === 'ArrowRight'){ idx = (idx+1) % links.length; links[idx].focus(); }
    if(e.key === 'ArrowLeft'){ idx = (idx-1+links.length) % links.length; links[idx].focus(); }
  });
});
