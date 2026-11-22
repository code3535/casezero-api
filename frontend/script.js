
// ==========================================
// CASEZERO - FRONTEND / BACKEND CONNECTION
// ==========================================

const API_URL = "http://127.0.0.1:8000";

// GLOBAL DATA
let investigations = [];
let suspects = [];
let clues = [];
let selectedInvestigation = null;


// ==========================================
// API HELPER
// ==========================================

async function apiRequest(endpoint, method = "GET", data = null) {
    const options = {
        method: method,
        headers: {
            "Content-Type": "application/json"
        }
    };

    if (data !== null) {
        options.body = JSON.stringify(data);
    }

    const response = await fetch(API_URL + endpoint, options);

    if (!response.ok) {
        const error = await response.json().catch(() => ({}));
        throw new Error(error.detail || `Request failed: ${response.status}`);
    }

    return response.json();
}


// ==========================================
// GET HTML ELEMENTS
// ==========================================

const investigationList = document.getElementById("investigation-list");
const suspectList = document.getElementById("suspect-list");
const suspectSelect = document.getElementById("suspect-select");
const questionInput = document.getElementById("question");
const askButton = document.getElementById("ask-button");
const answerBox = document.getElementById("answer");


// ==========================================
// DISPLAY MESSAGE
// ==========================================

function showMessage(element, message) {
    if (element) {
        element.textContent = message;
    }
}


// ==========================================
// LOAD CASE FROM BACKEND
// ==========================================

async function loadCase() {
    try {
        const caseData = await apiRequest("/case");

        selectedInvestigation = caseData;

        if (investigationList) {
            investigationList.innerHTML = "";

            const card = document.createElement("div");
            card.className = "case-card";

            const title = document.createElement("h3");
            title.textContent = caseData.title || caseData.name || "Current Investigation";

            const description = document.createElement("p");
            description.textContent = caseData.description || "Investigate the case and discover the truth.";

            card.appendChild(title);
            card.appendChild(description);

            investigationList.appendChild(card);
        }

        const caseCount = document.getElementById("case-count");

        if (caseCount) {
            caseCount.textContent = "1 CASE";
        }

    } catch (error) {
        console.error("Could not load case:", error);
    }
}


// ==========================================
// LOAD SUSPECTS FROM BACKEND
// ==========================================

async function loadSuspects() {
    try {
        suspects = await apiRequest("/suspects");

        displaySuspects();

    } catch (error) {
        console.error("Could not load suspects:", error);
    }
}


// ==========================================
// DISPLAY SUSPECTS
// ==========================================

function displaySuspects() {
    if (suspectList) {
        suspectList.innerHTML = "";
    }

    if (suspectSelect) {
        suspectSelect.innerHTML =
            '<option value="">Choose a suspect</option>';
    }

    suspects.forEach(function (suspect) {
        const id = suspect.suspect_id;

        if (suspectList) {
            const card = document.createElement("div");
            card.className = "suspect-card";

            const name = document.createElement("h3");
            name.textContent = suspect.name;

            const role = document.createElement("p");
            role.textContent = suspect.role || "Suspect";

            const description = document.createElement("p");
            description.textContent = suspect.description || "";

            const button = document.createElement("button");
            button.className = "select-button";
            button.textContent = "Select Suspect";

            button.addEventListener("click", function () {
                if (suspectSelect) {
                    suspectSelect.value = id;
                }

                document.getElementById("interrogation")?.scrollIntoView({
                    behavior: "smooth"
                });
            });

            card.appendChild(name);
            card.appendChild(role);
            card.appendChild(description);
            card.appendChild(button);

            suspectList.appendChild(card);
        }

        if (suspectSelect) {
            const option = document.createElement("option");

            option.value = id;
            option.textContent = suspect.name;

            suspectSelect.appendChild(option);
        }
    });
}


// ==========================================
// INTERROGATE SUSPECT
// ==========================================

if (askButton) {
    askButton.addEventListener("click", async function () {
        const suspectId = Number(suspectSelect?.value);
        const question = questionInput?.value.trim();

        if (!suspectId) {
            showMessage(answerBox, "Please select a suspect first.");
            return;
        }

        if (!question) {
            showMessage(answerBox, "Please enter a question.");
            return;
        }

        try {
            askButton.disabled = true;
            showMessage(answerBox, "The suspect is answering...");

            const result = await apiRequest("/ask", "POST", {
                suspect_id: suspectId,
                question: question
            });

            showMessage(
                answerBox,
                `${result.suspect_name}: ${result.answer}`
            );

            questionInput.value = "";

        } catch (error) {
            console.error("Interrogation error:", error);
            showMessage(answerBox, "Could not contact the backend: " + error.message);

        } finally {
            askButton.disabled = false;
        }
    });
}


// ==========================================
// CREATE INVESTIGATION SECTION
// ==========================================

function createInvestigationControls() {
    let section = document.getElementById("investigation-tools");

    if (section) return section;

    section = document.createElement("section");
    section.id = "investigation-tools";

    section.innerHTML = `
        <h2>Investigate Locations</h2>

        <p>Select a location to search for clues.</p>

        <select id="location-select">
            <option value="">Choose a location</option>
        </select>

        <button id="investigate-button">Investigate</button>

        <div id="investigation-result" class="answer">
            Your discovered clues will appear here.
        </div>

        <h2>Discovered Clues</h2>

        <div id="clue-list"></div>

        <h2>Final Accusation</h2>

        <p>Who do you think is responsible?</p>

        <select id="accusation-select">
            <option value="">Choose a suspect</option>
        </select>

        <button id="accuse-button">Make Final Accusation</button>

        <div id="accusation-result" class="answer">
            Your accusation result will appear here.
        </div>
    `;

    document.querySelector("main")?.appendChild(section);

    return section;
}


// ==========================================
// LOAD CLUES FROM BACKEND
// ==========================================

async function loadClues() {
    try {
        clues = await apiRequest("/clues");

        const locationSelect = document.getElementById("location-select");

        if (locationSelect) {
            locationSelect.innerHTML =
                '<option value="">Choose a location</option>';

            const locations = [
                ...new Set(
                    clues.map(clue => clue.found_at).filter(Boolean)
                )
            ];

            locations.forEach(function (location) {
                const option = document.createElement("option");

                option.value = location;
                option.textContent = location;

                locationSelect.appendChild(option);
            });
        }

    } catch (error) {
        console.error("Could not load clues:", error);
    }
}


// ==========================================
// INVESTIGATE LOCATION
// ==========================================

async function investigateLocation() {
    const location = document.getElementById("location-select")?.value;
    const resultBox = document.getElementById("investigation-result");

    if (!location) {
        showMessage(resultBox, "Please choose a location.");
        return;
    }

    try {
        const result = await apiRequest("/investigate", "POST", {
            location: location
        });

        showMessage(
            resultBox,
            result.message +
            (result.clue ? "\n" + JSON.stringify(result.clue, null, 2) : "")
        );

        await loadDiscoveredClues();

    } catch (error) {
        console.error("Investigation error:", error);
        showMessage(resultBox, error.message);
    }
}


// ==========================================
// LOAD DISCOVERED CLUES
// ==========================================

async function loadDiscoveredClues() {
    try {
        const discovered = await apiRequest("/discovered-clues");

        const clueList = document.getElementById("clue-list");

        if (!clueList) return;

        clueList.innerHTML = "";

        if (discovered.length === 0) {
            clueList.textContent = "No clues discovered yet.";
            return;
        }

        discovered.forEach(function (clue) {
            const card = document.createElement("div");
            card.className = "suspect-card";

            const title = document.createElement("h3");
            title.textContent = clue.name || clue.title || `Clue ${clue.clue_id}`;

            const description = document.createElement("p");
            description.textContent = clue.description || "New clue discovered.";

            card.appendChild(title);
            card.appendChild(description);

            clueList.appendChild(card);
        });

    } catch (error) {
        console.error("Could not load discovered clues:", error);
    }
}


// ==========================================
// FINAL ACCUSATION
// ==========================================

async function makeAccusation() {
    const suspectId = Number(
        document.getElementById("accusation-select")?.value
    );

    const resultBox = document.getElementById("accusation-result");

    if (!suspectId) {
        showMessage(resultBox, "Please select a suspect.");
        return;
    }

    try {
        const result = await apiRequest("/accuse", "POST", {
            suspect_id: suspectId
        });

        if (result.correct) {
            showMessage(
                resultBox,
                "CORRECT! " + result.message +
                "\nSuspect: " + result.suspect +
                "\nMotive: " + result.motive +
                "\nExplanation: " + result.explanation
            );
        } else {
            showMessage(resultBox, result.message);
        }

    } catch (error) {
        console.error("Accusation error:", error);
        showMessage(resultBox, error.message);
    }
}


// ==========================================
// CONNECT BUTTONS
// ==========================================

function connectInvestigationButtons() {
    document.getElementById("investigate-button")
        ?.addEventListener("click", investigateLocation);

    document.getElementById("accuse-button")
        ?.addEventListener("click", makeAccusation);

    const accusationSelect =
        document.getElementById("accusation-select");

    if (accusationSelect) {
        suspects.forEach(function (suspect) {
            const option = document.createElement("option");

            option.value = suspect.suspect_id;
            option.textContent = suspect.name;

            accusationSelect.appendChild(option);
        });
    }
}


// ==========================================
// INITIALIZE APPLICATION
// ==========================================

async function initializeApp() {
    try {
        console.log("Connecting to CaseZero backend...");

        await loadCase();
        await loadSuspects();

        createInvestigationControls();

        await loadClues();
        await loadDiscoveredClues();

        connectInvestigationButtons();

        console.log("CaseZero frontend initialized successfully!");

    } catch (error) {
        console.error("Application initialization failed:", error);
    }
}

initializeApp();
