class Hospital:
    """Represents a hospital that manages doctors, patients, and appointments."""

    def __init__(self, name):
        # Hospital name
        self.name = name

        # Stores all hired doctors
        self.doctors = []

        # Stores all registered patients
        self.patients = []

        # Stores all scheduled appointments
        self.appointments = []

    def find_doctor(self, doc_id):
        """Search for a doctor using the doctor ID."""

        for doc in self.doctors:
            if doc.doctor_id == doc_id:
                return doc

        return False

    def find_patient(self, patient_id):
        """Search for a patient using the patient ID."""

        for patient in self.patients:
            if patient.patient_id == patient_id:
                return patient

        return False

    def hire_doctor(self, doctor):
        """
        Adds a new doctor to the hospital.

        Returns False if a doctor with the same
        ID already exists.
        """

        new_doc = self.find_doctor(doctor.doctor_id)

        if new_doc:
            return False

        self.doctors.append(doctor)
        return True

    def register_patient(self, patient):
        """
        Registers a new patient.

        Returns False if the patient
        is already registered.
        """

        reg_patient = self.find_patient(patient.patient_id)

        if reg_patient:
            return False

        self.patients.append(patient)
        return True

    def schedule_appointment(self, date, time, doctor, patient):
        """
        Schedules an appointment between
        a doctor and a patient.

        Returns False if the doctor is
        unavailable at the given date and time.
        """

        doc = self.find_doctor(doctor.doctor_id)

        if not doc:
            return False

        for appoint in self.appointments:

            if (
                appoint.doctor.doctor_id == doctor.doctor_id
                and appoint.date == date
                and appoint.time == time
            ):
                return False

        appointment = Appointment(
            date,
            time,
            doctor,
            patient
        )

        self.appointments.append(appointment)

        return True

    def show_appointments(self):
        """Displays all scheduled appointments."""

        if not self.appointments:
            print("There are no appointments yet.\n")

        else:
            for appoint in self.appointments:

                print(f"Doctor ID : {appoint.doctor.doctor_id}")
                print(f"Patient ID: {appoint.patient.patient_id}")
                print("Appointment Time")
                print(f"Date: {appoint.date} at {appoint.time}")
                print()


class Doctor:
    """Represents a doctor."""

    def __init__(self, doctor_id, doctor_name):
        self.doctor_id = doctor_id
        self.doctor_name = doctor_name


class Patient:
    """Represents a patient."""

    def __init__(self, patient_id, patient_name):
        self.patient_id = patient_id
        self.patient_name = patient_name


class Appointment:
    """Represents an appointment between a doctor and a patient."""

    def __init__(self, date, time, doctor, patient):
        self.date = date
        self.time = time
        self.doctor = doctor
        self.patient = patient


# ---------------------------- MAIN PROGRAM ---------------------------- #

hospital = Hospital("APOLLO HOSPITAL")

while True:

    # Display menu
    print(
        "1.Hire Doctor\n"
        "2.Register Patient\n"
        "3.Schedule Appointment\n"
        "4.Find Doctor\n"
        "5.Find Patient\n"
        "6.Show Appointments\n"
        "7.Exit"
    )

    choose = int(input("Choose (1-7): "))

    # Hire a doctor
    if choose == 1:

        doc_name = input(
            "Enter the doctor's name: "
        ).title()

        doc_id = int(
            input("Enter doctor ID: ")
        )

        doctor = Doctor(
            doctor_id=doc_id,
            doctor_name=doc_name
        )

        if hospital.hire_doctor(doctor):
            print("Doctor appointed successfully.\n")
        else:
            print("Doctor ID already exists.\n")

    # Register a patient
    elif choose == 2:

        pat_id = int(
            input("Enter patient ID: ")
        )

        pat_name = input(
            "Enter patient name: "
        ).title()

        patient = Patient(
            patient_id=pat_id,
            patient_name=pat_name
        )

        if hospital.register_patient(patient):
            print("Patient registered successfully.\n")
        else:
            print("Patient already registered.\n")

    # Schedule appointment
    elif choose == 3:

        doc_id = int(
            input("Enter doctor ID: ")
        )

        pat_id = int(
            input("Enter patient ID: ")
        )

        doctor = hospital.find_doctor(doc_id)
        patient = hospital.find_patient(pat_id)

        date = input("Enter date: ")
        time = input("Enter time: ")

        if hospital.schedule_appointment(
            date=date,
            time=time,
            doctor=doctor,
            patient=patient
        ):
            print(
                f"Appointment scheduled "
                f"on {date} at {time}.\n"
            )
        else:
            print("Doctor is unavailable.\n")

    # Find doctor
    elif choose == 4:

        doc_id = int(input("Enter doctor ID: "))

        doctor = hospital.find_doctor(doc_id)

        if doctor:
            print(f"Doctor Name: {doctor.doctor_name}\n")
        else:
            print("Doctor not found.\n")

    # Find patient
    elif choose == 5:

        patient_id = int(
            input("Enter patient ID: ")
        )

        patient = hospital.find_patient(patient_id)

        if patient:
            print(f"Patient Name: {patient.patient_name}\n")
        else:
            print("Patient not found.\n")

    # Show appointments
    elif choose == 6:

        hospital.show_appointments()

    # Exit
    elif choose == 7:

        print("Exiting...")
        break

    else:
        print("Please choose a number between 1 and 7.\n")