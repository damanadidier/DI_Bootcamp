Build a web application for church member management for 
"Eglise Protestante Evangélique – Vie Chrétienne Victorieuse" (EPE-VCV).

=== TECH STACK ===
- React for frontend (using Create React App)
- Language: French UI (all labels in French)

=== DATA MODEL ===

Create a `Member` model with these fields:

PERSONAL INFO:
- photo (ImageField, optional)
- last_name (CharField)
- first_name (CharField)
- gender (CharField, choices: Homme / Femme)
- date_of_birth (DateField)
- place_of_birth (CharField)
- community (CharField — the local church branch attended)
- role_in_church (CharField — e.g. Diacre, Ancien, Membre, etc.)
- baptism_date (DateField, nullable)
- epvcv_join_date (DateField — date d'adhésion EPE-VCV)

MARITAL STATUS:
- marital_status (CharField, choices: Célibataire, Marié(e), Veuf/Veuve, Divorcé(e))
- spouse_name (CharField, optional)
- number_of_children (IntegerField, default=0)
- id_number (CharField — CNI / Passeport number)

CONTACT:
- phone_1 (CharField)
- phone_2 (CharField, optional)
- email (EmailField, optional)

PROFESSIONAL INFO:
- profession (CharField)
- job_title (CharField — Fonction)
- diploma (CharField — highest diploma)
- specialization (CharField)
- activity_sector (CharField)

SOCIAL STATUS (BooleanFields or CharField choices):
- social_status (CharField, choices: Chef d'entreprise, Employé permanent, 
  Fonctionnaire, Employé occasionnel, Indépendant, Artisan)
- activity_start_date (DateField, nullable)
- years_of_experience (IntegerField, nullable)

DOCUMENTS:
- id_document_copy (FileField, optional — CNI/Passport copy)
- baptism_certificate (FileField, optional)

METADATA:
- created_at (auto DateTimeField)
- updated_at (auto DateTimeField)
- validated_by_pastor (BooleanField, default=False)
- member_number (auto-generated unique ID)

=== FEATURES TO BUILD ===

1. MEMBER REGISTRATION FORM
   - Multi-step form (3 steps): Personal Info → Professional Info → Documents
   - Progress bar showing current step
   - Photo upload with preview
   - File upload for CNI copy and baptism certificate
   - Form validation with French error messages
   - On submit: show a printable membership card summary

2. MEMBER LIST / DASHBOARD
   - Paginated table of all members
   - Search by name, community, role
   - Filter by: gender, marital status, social status, community
   - Export to CSV and PDF buttons
   - Stats cards at top: Total members, Men, Women, Baptized

3. MEMBER DETAIL PAGE
   - Full profile view with all fields
   - Edit and Delete buttons (admin only)
   - Pastor validation toggle
   - Print profile button

4. ADMIN PANEL
   - Customize Django admin to show all fields
   - List display with search and filters
   - Bulk export action

5. AUTHENTICATION
   - Login page (French labels)
   - Role-based access: Pastor (full access), Secretary (add/edit), Member (view own)
   - Custom User model extending AbstractUser with `role` field

6. PRINTABLE MEMBERSHIP CARD
   - Auto-generated member card (HTML/CSS print view) with:
     photo, full name, member number, community, role, baptism date, join date
   - Print CSS media query for clean output

=== UI DESIGN ===
- Colors: Deep navy blue (#1a2e5a) + Gold accent (#c9a84c) to reflect church dignity
- Font: Clean sans-serif (Nunito or Lato via Google Fonts)
- Church name and logo placeholder in header
- Responsive (works on mobile for field data entry)
- All UI labels in French



=== EXTRA NOTES ===
- Generate a unique member number like: EPE-VCV-2026-0001
- All date formats: DD/MM/YYYY (French standard)
- Use the attached logo.png as a placeholder for the church logo in the header
- Ensure all forms and pages are in French with appropriate labels and error messages
- Add also logo to the login page for better branding and favicon.