// TEMPORARY MOCK DATA
// We will replace this with FastAPI requests later.
const API_URL = "http://192.168.1.70:8000";
async function testConnection() {
    try {
        const response = await fetch(API_URL + "/docs");

        console.log("Backend connected!", response.status);
    } catch (error) {
        console.log("Connection failed:", error);
    }
}

testConnection();

const investigations = [
    {
        id: 101,
        title: "The Missing Documents",
        description: "Confidential company documents disappeared from a secured office.",
        status: "Active",
        suspects: [
            {
                id: 1,
                name: "James Carter",
                role: "Security Guard",
                description: "Was responsible for monitoring the building."
            },
            {
                id: 2,
                name: "Sarah Mitchell",
                role: "Office Manager",
                description: "Had access to the confidential documents."
            }
        ]
    },
    {
        id: 102,
        title: "The Museum Mystery",
        description: "A valuable historical artifact disappeared during an exhibition.",
        status: "Active",
        suspects: [
            {
                id: 3,
                name: "David Wilson",
                role: "Museum Employee",
                description: "Worked in the exhibition area."
            }
        ]
    },
    {
        id: 103,
        title: "The Office Incident",
        description: "An unexplained incident occurred after office hours.",
        status: "Pending",
        suspects: [
            {
                id: 4,
                name: "Michael Brown",
                role: "Employee",
                description: "Was among the last people to leave."
            }
        ]
    }
];

let selectedInvestigation = investigations[0];

// GET HTML ELEMENTS
const investigationList =
    document.getElementById("investigation-list");

const suspectList =
    document.getElementById("suspect-list");

const suspectSelect =
    document.getElementById("suspect-select");

const questionInput =
    document.getElementById("question");

const askButton =
    document.getElementById("ask-button");

const answerBox =
    document.getElementById("answer");

// DISPLAY INVESTIGATIONS
function displayInvestigations() {
    investigationList.innerHTML = "";

    document.getElementById("case-count").textContent =
        investigations.length + " CASES";

    investigations.forEach(function (investigation) {
        const card = document.createElement("div");

        card.className = "case-card";

        card.innerHTML = `
            <span class="case-status">
                ${investigation.status}
            </span>

            <h3>${investigation.title}</h3>

            <p>${investigation.description}</p>

            <p>Suspects: ${investigation.suspects.length}</p>

            <button class="select-button">
                View Investigation
            </button>
        `;

        card.querySelector("button").addEventListener("click", function () {
            selectInvestigation(investigation.id);
        });

        investigationList.appendChild(card);
    });
}

// SELECT INVESTIGATION
function selectInvestigation(id) {
    selectedInvestigation = investigations.find(function (item) {
        return item.id === id;
    });

    displaySuspects();

    document.getElementById("suspects").scrollIntoView({
        behavior: "smooth"
    });
}

// DISPLAY SUSPECTS
function displaySuspects() {
    suspectList.innerHTML = "";
    suspectSelect.innerHTML = '<option value="">Choose a suspect</option>';

    selectedInvestigation.suspects.forEach(function (suspect) {
        const card = document.createElement("div");

        card.className = "suspect-card";

        card.innerHTML = `
            <h3>${suspect.name}</h3>
            <p>${suspect.role}</p>
            <p>${suspect.description}</p>
            <button class="select-button">Select Suspect</button>
        `;

        card.querySelector("button").addEventListener("click", function () {
            suspectSelect.value = suspect.id;

            document.getElementById("interrogation").scrollIntoView({
                behavior: "smooth"
            });
        });

        suspectList.appendChild(card);

        const option = document.createElement("option");

        option.value = suspect.id;
        option.textContent = suspect.name;

        suspectSelect.appendChild(option);
    });
}

// ASK SUSPECT A QUESTION
askButton.addEventListener("click", function () {
    const suspectId = Number(suspectSelect.value);
    const question = questionInput.value.trim();

    if (!suspectId) {
        answerBox.textContent = "Please select a suspect first.";
        return;
    }

    if (!question) {
        answerBox.textContent = "Please enter a question.";
        return;
    }

    const suspect = selectedInvestigation.suspects.find(function (item) {
        return item.id === suspectId;
    });

    // Temporary response until backend integration.
    answerBox.textContent =
        "Demo mode: Your question for " + suspect.name +
        ' was "' + question +
        '". The real interrogation response will come from the CaseZero API.';

    questionInput.value = "";
});

// INITIALIZE FRONTEND
displayInvestigations();
displaySuspects();