import random
from datetime import datetime, timedelta
from faker import Faker
import pandas as pd

# number of records
PROD_RECORD = 100
#initialize faker
fake = Faker()

# a function to generate patients data
def generate_patients_data(num_records):
  patients_data =[]
  for _ in range(num_records):
    patient_data =(
        {
            'patient_id': fake.uuid4(),
            'patient_name':fake.name(),
            'gender':random.choice(['Male','Female','Other']),
            'date_of_birth':fake.date_of_birth(minimum_age=18,maximum_age=80).strftime('%Y-%m-%d'),
            'email':fake.email(),
            'phone_number':fake.phone_number()

        }
    )
    patients_data.append(patient_data)
  return pd.DataFrame(patients_data)
  

# a function to generate doctor data
def generate_doctors_data(num_records):
  doctors_data=[]
  for _ in range(num_records):
    doctor_data={
        'doctor_id':fake.uuid4(),
        'doctor_name':fake.name(),
        'specialization':random.choice(['Cardiology','Dermatology','Orthopedics','Pediatrics','Gastroenterology']),
        'email':fake.email(),
        'phone_number':fake.phone_number()
    }
    doctors_data.append(doctor_data)
  return pd.DataFrame(doctors_data)
  

# a fucntion to generate appointment data
def generate_appointments_data(num_records,patient_id,doctor_id):
  appointments_data=[]
  for _ in range(num_records):
    appointment_data={
        'appointment_id':fake.uuid4(),
        'patient_id':random.choice(patient_id),
        'doctor_id':random.choice(doctor_id),
        'appointment_date':fake.date_between(start_date='-1y',end_date='today').strftime('%Y-%m-%d'),
        'status':random.choice(['Scheduled','Completed','Cancelled'])
    }
    appointments_data.append(appointment_data)
  return pd.DataFrame(appointments_data)
  


# generate medical record data
def generate_medical_records_data(num_records,patient_id):
  medical_records_data=[]
  for _ in range(num_records):
    medical_record_data={
        'record_id':fake.uuid4(),
        'patient_id':random.choice(patient_id),
        'record_date':fake.date_between(start_date='-1y',end_date='today').strftime('%Y-%m-%d'),
        'diagnosis':fake.text(),
        'treatment':fake.text(),
        'precription':fake.text(),
        'notes':fake.text()
    }
    medical_records_data.append(medical_record_data)


  return pd.DataFrame(medical_records_data)
  

# generate billing data/invoices
def generate_invoice_data(num_records,patient_id):
  invoices_data=[]

  for _ in range(num_records):
    invoice_data={
        'invoice_id':fake.uuid4(),
        'patient_id':random.choice(patient_id),
        'invoice_date':fake.date_between(start_date='-1y',end_date='today').strftime('%Y-%m-%d'),
        'amount':round(random.uniform(50,500),2),
        'payment_method':random.choice(['Credit Card','Debit Card','Cash']),
        'payment_status':random.choice(['Paid','Unpaid']),
        'date_issued':fake.date_between(start_date='-1y',end_date='today').strftime('%Y-%m-%d')
    }
    invoices_data.append(invoice_data)
  return pd.DataFrame(invoices_data)
 

# patients dataset
patients_df = generate_patients_data(PROD_RECORD)
patients_df.to_csv('health_data/patients.csv',index=False)
print('Patients data generated successfully!')

# doctors dataset
doctors_df=generate_doctors_data(PROD_RECORD)
doctors_df.to_csv('health_data/doctors.csv',index=False)
print('Doctors data generated successfully!')

# appointments dataset
appointments_df=generate_appointments_data(PROD_RECORD,patients_df['patient_id'],doctors_df['doctor_id'])
appointments_df.to_csv('health_data/appointments.csv',index=False)
print('Appointments data generated successfully!')

# Medical records data set
medical_records_df=generate_medical_records_data(PROD_RECORD,patients_df['patient_id'])
medical_records_df.to_csv('health_data/medical_records.csv',index=False)
print('Medical records data generated successfully!')

# invoice dataset
invoices_df=generate_invoice_data(PROD_RECORD,patients_df['patient_id'])
invoices_df.to_csv('health_data/invoices.csv',index=False)
print('Invoices data generated successfully!')

# The above code generates fake data for a healthcare system, including patients, doctors, appointments, medical records, and invoices.


