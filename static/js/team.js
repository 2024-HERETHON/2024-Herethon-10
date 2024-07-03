const Addteam = document.querySelector('.add_team');
const todoModify = document.querySelector('.todo_modify');

function findFriend() {
    if(Addteam.classList[1] === 'none'){
        Addteam.classList.remove('none');
    } else {
        Addteam.classList.add('none');
    }
}

function modifyTodo() {
    if(todoModify.classList[1] === 'none'){
        todoModify.classList.remove('none');
    } else {
        todoModify.classList.add('none');
    }
}

