console.log("Never");

// Data about us

const data = [

    {       
        name : 'Md. Mohsin Uddin',
        work: 'Instructor of the project',
        city : 'Lives in Dhaka',
        language: 'Research Interest: Machine learning, Natural Language Processing (NLP)',
        uni : 'Lecturer at East West University',
        linkedIn : 'Faculty of Computer Sciences and Engineering',
        github : 'Email: mmuddin@ewubd.edu ',
        image : '/static/images/sir.jpg'

    },

    {       
        name : 'Rakib Raihan Fahim',
        work:'Developer',
        city : 'Hometown: Khulna',
        language: 'Primariliy works on Python, Javascript, C, C++, HTML, CSS',
        uni : 'Student at East West University',
        linkedIn : 'LinkedIn: https://www.linkedin.com/in/rakib-raihan-fahim-967b7a176/',
        github : 'Github: https://github.com/RyanFahim',
        image : '/static/images/fahim.jpg'

    },
    {       
        name : 'Halima Begum',
        work:'Developer',
        city : 'Hometown: Bogra',
        language: 'Primariliy works on Python, Javascript, C, C++, HTML, CSS',
        uni : 'Student at East West University',
        linkedIn : 'https://www.linkedin.com/in/rakib-raihan-fahim-967b7a176/',
        github : 'https://github.com/RyanFahim',
        image : '/static/images/halum.jpg'

    }
]

function proIterator(profiles){
    let nextIndex = 0;
    return {
        next: function(){
            return nextIndex<profiles.length ?
            {value: profiles[nextIndex++], done: false}:
            {done: true}
        }
    };
}

// button for next developer
const developer = proIterator(data)
nextDevloper();

const next = document.getElementById('next');
next.addEventListener('click', nextDevloper);

function nextDevloper(){
    const currentDeveloper = developer.next().value;

    let image = document.getElementById('image');
    let profile = document.getElementById('profile');
    if(currentDeveloper != undefined){ 
    image.innerHTML = `<br><image src='${currentDeveloper.image}' style="border-radius: 100px;" >`;
    profile.innerHTML = `<ul class="list-group">
    <li class="list-group-item list-group-item-success"<h2>${currentDeveloper.name}</h2></li>
    <li class="list-group-item">${currentDeveloper.work}</li>
    <li class="list-group-item">${currentDeveloper.language}</li>  
    <li class="list-group-item">${currentDeveloper.uni}</li>
    <li class="list-group-item">${currentDeveloper.linkedIn}</li>
    <li class="list-group-item">${currentDeveloper.github}</li>
    <li class="list-group-item">${currentDeveloper.city}</li>
    
  </ul>`;
    }
    else {
        alert('End of the developers');
        window.location.reload();
    }
}
