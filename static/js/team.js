const Addteam = document.querySelector('.add_team');
const todoModify = document.querySelector('.todo_modify');

// gsap 기본 상태
gsap.set(Addteam, { bottom: '-400px' });
gsap.set(todoModify, { bottom: '-400px' });

function findFriend() {
    if(Addteam.classList[1] === 'none'){
        Addteam.classList.remove('none');
        gsap.to('.add_team', { duration: 1, bottom: "0", ease: "power3.out"});
    } else {
        Addteam.classList.add('none');
        gsap.set(Addteam, { bottom: '-400px' });
    }
}

function modifyTodo() {
    if(todoModify.classList[1] === 'none'){
        todoModify.classList.remove('none');
        gsap.to('.todo_modify', { duration: 1, bottom: "0", ease: "power3.out"});
    } else {
        todoModify.classList.add('none');
        gsap.set(todoModify, { bottom: '-400px' });
    }
}

