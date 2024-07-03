const Popup = document.querySelector('.popup_wrap');
const No = document.querySelector('.no');
const addTeam = document.querySelector('.add_team');
const First = document.querySelector('.first');
const Second = document.querySelector('.second');

function showPop() {
    Popup.classList.remove('none');
}

function noPop() {
    Popup.classList.add('none');
}

// gsap 기본 상태
gsap.set(addTeam, { bottom: '-400px' });

function addFriend() {
    addTeam.classList.remove('none');
    gsap.to('.add_team', { duration: 1, bottom: "0", ease: "power3.out"});
}

function teamName() {
    First.classList.add('none');
    Second.classList.remove('none');
}

// document.addEventListener('DOMContentLoaded', function () {
//     const main = document.getElementById('main');
//     const teams = [
//         { href: './template/team.html', day: 'D-17', percent: '60%' },
//         { href: '', day: 'D-17', percent: '60%' },
//         { href: '', day: 'D-17', percent: '60%' }
//     ];

//     teams.forEach(team => {
//         const anchor = document.createElement('a');
//         anchor.href = team.href;

//         const box = document.createElement('div');
//         box.classList.add('box');

//         const top = document.createElement('div');
//         top.classList.add('top');
//         const h2 = document.createElement('h2');
//         h2.textContent = '여기톤 10조';
//         const profileBox = document.createElement('div');
//         profileBox.classList.add('profile_box');
//         for (let i = 0; i < 5; i++) {
//             const profile = document.createElement('div');
//             profile.classList.add('profile', `profile0${i + 1}`);
//             profileBox.appendChild(profile);
//         }
//         top.appendChild(h2);
//         top.appendChild(profileBox);

//         const middle = document.createElement('div');
//         middle.classList.add('middle');
//         const graph = document.createElement('div');
//         graph.classList.add('graph');
//         const canvas = document.createElement('canvas');
//         canvas.id = 'doughnut-chart';
//         canvas.width = 100;
//         canvas.height = 100;
//         graph.appendChild(canvas);
//         middle.appendChild(graph);

//         const bottom = document.createElement('div');
//         bottom.classList.add('bottom');
//         const day = document.createElement('div');
//         day.classList.add('day');
//         day.textContent = team.day;
//         const percent = document.createElement('div');
//         percent.classList.add('parcent');
//         percent.textContent = team.percent;
//         bottom.appendChild(day);
//         bottom.appendChild(percent);

//         box.appendChild(top);
//         box.appendChild(middle);
//         box.appendChild(bottom);

//         anchor.appendChild(box);
//         main.appendChild(anchor);
//     });

//     // 차트 생성
//     new Chart(document.getElementById("doughnut-chart"), {
//         type: 'doughnut',
//         data: {
//             datasets: [
//                 {
//                     backgroundColor: ["var(--gray)", "var(--gray)", "var(--gray)", "var(--gray)", "#C22370"],
//                     data: [10, 20, 10, 10, 50]
//                 }
//             ]
//         },
//     });
// });