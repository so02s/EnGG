# EnGG - English Learning App

**EnGG** is a mobile app, fork from **Engrisk**. This project start for fun only.

## 🖼️ Screenshots

| Home Screen | Lesson List | Vocabulary Topic | Flashcards | Progress |
|---|---|---|---|---|
| ![image](https://github.com/user-attachments/assets/d8bb75e2-e970-41c8-9173-1fb7434c32d6) | ![image](https://github.com/user-attachments/assets/88e238f6-0947-49ff-b651-4240b1272d17) | ![image](https://github.com/user-attachments/assets/bea0c573-9814-4c04-8dbe-6db808727c89) | ![image](https://github.com/user-attachments/assets/572592b1-a9d1-4daf-926d-bf5267b527af) | ![image](https://github.com/user-attachments/assets/6b396680-4742-4d1c-b6c2-48ea17fa21ba) |

## ✨ Features

The Engrisk application includes the following core feature flows:

#### 👤 **User Authentication & Management**
* Register, Login, and Auto-Login sessions.
* Full Profile Management:
    * View user information.
    * Update display name.
    * Change password (with re-authentication for security).
    * Permanently delete account (includes Firestore data cleanup).
    * Logout functionality.

#### 📚 **Structured Lessons**
* Lessons categorized into 3 levels: Beginner, Intermediate, and Advanced.
* **Diverse Exercise Types:**
    * Translation (Vietnamese-English & English-Vietnamese).
    * Listen & Fill-in-the-blank.
    * Listen & Choose the correct answer.
* Automatically saves scores and progress after completing each lesson.

#### 📇 **Vocabulary Learning with Flashcards**
* Learn vocabulary organized by topics (Animals, Food, Jobs, etc.).
* Modern flashcard interface with **3D flip animation** and **swipe navigation**.
* Integrated **Text-to-Speech** to listen to standard pronunciation of words.
* Saves learning progress: Users can mark words as **"I know"** or **"I don't know"**.

#### 📈 **Progress Tracking**
* **Overview Dashboard:** Displays statistics on completed lessons and learned words.
* **Detailed Lesson History:** Shows a list of completed lessons with scores and completion dates.
* **Detailed Vocabulary History:** Displays a list of learned words.
* **Interactive:** Allows users to tap on a lesson in their history to redo it.
* (Future plan) Allows users to tap on a voca in their history to see overview of it such as word, meaning, definition, pronunciation, mark word as learned or for learning, ...

## 🛠️ Tech Stack & Architecture

This project was built using modern technologies and architecture patterns recommended by Google.

* **Language:** **Kotlin** (Official language for Android development).
* **Architecture:**
    * **Single-Activity Architecture:** Utilizes a main Activity to host all Fragments.
    * **Lean MVVM (Model-View-ViewModel):** Separates UI (View) from data (Model), using a `SharedViewModel` to share user state across the app.
* **UI:**
    * **Android XML** with ViewBinding.
    * **Material Design 3:** Implements modern components like `MaterialCardView`, `MaterialButton`, `BottomNavigationView`.
* **Jetpack Components:**
    * **Navigation Component:** Manages all navigation flows between screens visually and efficiently.
    * **ViewModel & LiveData:** Manages UI-related data in a lifecycle-aware way.
* **Backend & Data:**
    * **Firebase Authentication:** Handles user authentication.
    * **Cloud Firestore:** NoSQL database for storing all user info, lessons, vocabulary, and progress.
* **Third-party Libraries:**
    * **Glide:** For loading and displaying images from the internet.
    * **Android's built-in Text-to-Speech (TTS)** engine.

## 🚀 Getting Started

1.  Clone this repository to your local machine.
2.  Open the project in Android Studio.
3.  Create a new project on the [Firebase Console](https://console.firebase.google.com/).
4.  Add an Android app to the Firebase project with the package name `com.dex.engrisk`.
5.  Download the `google-services.json` file from Firebase and place it in the project's `app` directory.
6.  In the Firebase Console, enable the following services: **Authentication** (with the Email/Password provider) and **Cloud Firestore**.
7.  Build and run the application.

## ✍️ Authors

* **[Dex]** - dwwwtan@gmail.com
* **[so02s]** - trying just do some fun (and prepare for english exams)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
