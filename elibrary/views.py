from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.http import HttpResponse
from django.db import models
from .models import subject
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Question, Answer, Comment, UpVote, DownVote
from django.core.paginator import Paginator
from .forms import AnswerForm, QuestionForm
from django.contrib import messages
from django.db.models import Count
from users.forms import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView,
	UpdateView,
	DeleteView
)

def subjectview_sem3(request): 
	DMA = subject()
	DMA.subject_name = 'DMA'
	DMA.pdf_link1 = 'DMA_unit1.pdf'
	DMA.pdf_link2 = 'DMA_unit2.pdf'
	DMA.pdf_link3 = 'DMA_unit3.pdf'
	DMA.pdf_link4 = 'DMA_unit4.pdf'
	DMA.pdf_link5 = 'DMA_unit5.pdf'

	DMA.content1 = 'Logic – Sets and Functions: Logic, Propositional equivalences – Predicates and Quantifiers – Nested Quantifiers-Rules of Inference-Sets-Set Operations, Functions.Integers: The Integers and Division, Integers and Algorithms, Applications of Number Theory'
	DMA.content2 = 'Mathematical Reasoning, Induction, and Recursion: Proof Strategy, Sequence and Summation, Mathematical Induction, Recursive Definitions and Structural Induction, Recursive Algorithms. Counting: Basics of Counting, Pigeonhole Principle, Permutations and Combinations– Binomial Coefficients, Generalized Permutations and Combinations, Generating Permutations and Combinations.'
	DMA.content3 = 'Advanced Counting Techniques: Recurrence Relations, Solving Linear Recurrence Relations, Divide and Conquer Algorithms and Recurrence Relations, Generating Functions, Inclusion–Exclusion, Application of Inclusion – Exclusion. Relations: Relations & their Properties, N-ary Relations and Applications, Representing Relations, Closures of Relations, Equivalence Relations, Partial Orderings.'
	DMA.content4 = 'Algebraic Structures: Algebraic System - General Properties, semi groups, Monoids, Homomorphism, Groups, Residue arithmetic, group codes and their applications.'
	DMA.content5 = 'Algebraic Structures: Algebraic System - General Properties, semi groups, Monoids, Homomorphism, Groups, Residue arithmetic, group codes and their applications.' 
		


	DSA = subject()
	DSA.subject_name = 'DSA'
	DSA.pdf_link1 = 'DMA_unit1.pdf'
	DSA.pdf_link2 = 'DMA_unit2.pdf'
	DSA.pdf_link3 = 'DMA_unit3.pdf'
	DSA.pdf_link4 = 'DMA_unit4.pdf'
	DSA.pdf_link5 = 'DMA_unit5.pdf'

	DSA.content1 = 'Logic – Sets and Functions: Logic, Propositional equivalences – Predicates and Quantifiers – Nested Quantifiers-Rules of Inference-Sets-Set Operations, Functions.Integers: The Integers and Division, Integers and Algorithms, Applications of Number Theory'
	DSA.content2 = 'Mathematical Reasoning, Induction, and Recursion: Proof Strategy, Sequence and Summation, Mathematical Induction, Recursive Definitions and Structural Induction, Recursive Algorithms. Counting: Basics of Counting, Pigeonhole Principle, Permutations and Combinations– Binomial Coefficients, Generalized Permutations and Combinations, Generating Permutations and Combinations.'
	DSA.content3 = 'Advanced Counting Techniques: Recurrence Relations, Solving Linear Recurrence Relations, Divide and Conquer Algorithms and Recurrence Relations, Generating Functions, Inclusion–Exclusion, Application of Inclusion – Exclusion. Relations: Relations & their Properties, N-ary Relations and Applications, Representing Relations, Closures of Relations, Equivalence Relations, Partial Orderings.'
	DSA.content4 = 'Algebraic Structures: Algebraic System - General Properties, semi groups, Monoids, Homomorphism, Groups, Residue arithmetic, group codes and their applications.'
	DSA.content5 = 'Algebraic Structures: Algebraic System - General Properties, semi groups, Monoids, Homomorphism, Groups, Residue arithmetic, group codes and their applications.' 

	BE = subject()
	BE.subject_name = 'BE'
	BE.pdf_link1 = 'BE_unit1.pdf'
	BE.pdf_link2 = 'BE_unit2.pdf'
	BE.pdf_link3 = 'BE_unit3.pdf'
	BE.pdf_link4 = 'BE_unit4.pdf'
	BE.pdf_link5 = 'BE_unit5.pdf'

	BE.content1 = 'Semiconductor Theory: Energy levels, Intrinsic and Extrinsic Semiconductor, Mobility, Diffusion and Drift current, Hall effect, Law of mass action, Characteristics of P-N Junction diode, current equation, Parameters and Applications. Rectifiers: Half wave and Full wave Rectifiers Bridge and center tapped with and without filters, Ripple factor, regulation and efficiency.'
	BE.content2 = 'Transistors: Bipolar and field effect transistors with their h-parameter equivalent circuits, Basic Amplifiers classification and their circuits (Qualitative treatment only). Regulators and Inverters: Zener Diode, Breakdown mechanisms, Characteristics, Effect of Temperature, Application as voltage regulator.'
	BE.content3 = 'Feedback Amplifiers: Properties of Negative Feedback Amplifier, Types of Negative Feedback, Effect of negative feedback on Input impedance and Output impedance, Applications (Qualitative treatment only). Oscillators: principle of oscillations, LC Type-Hartley, Colpitt and RC TypePhase shift, Wien Bridge and Crystal Oscillator (Qualitative treatment only).'
	BE.content4 = 'Operational Amplifiers: Basic Principle, Ideal and practical Characteristics and Applications-Summer, Integrator, Differentiator, Instrumentation Amplifier. Power Amplifiers: Operation of Class A, Class B, Class AB and Class C power amplifiers.'
	BE.content5 = 'Data Acquisition systems: Study of transducers-LVDT, Strain gauge. Photo Electric Devices and Industrial Devices: Photo diode, Photo Transistor, LED, LCD, SCR, UJT Construction and Characteristics and their applications only. Display Systems: Constructional details of C.R.O and Applications.'



	POM = subject()
	POM.subject_name = 'POM'
	POM.pdf_link1 = 'POM_unit1.pdf'
	POM.pdf_link2 = 'POM_unit2.pdf'
	POM.pdf_link3 = 'POM_unit3.pdf'
	POM.pdf_link4 = 'POM_unit4.pdf'
	POM.pdf_link5 = 'POM_unit5.pdf'

	POM.content1 = 'Management: Definition of management, science or art, manager vs entrepreneur; managerial roles and skills;. Evolution of management, Basic management theories by FW Taylor, Henry Fayol, Types of Business Organizations, sole proprietorship, partnership, company, public and private enterprises; Organization culture and environment; Current trends and issues in management.'
	POM.content2 = 'Planning: Nature and purpose of Planning, types of Planning, objectives, setting objectives, policies, Strategic Management, Planning Tools and Techniques, Planning plant location and layout, Decision making steps & processes.'
	POM.content3 = 'Organizing: Nature and purpose of Organizing, formal and informal organization, organization structure, types, line and staff authority, departmentalization, delegation of authority, centralization and decentralization, job design, human resource management, HR planning, Recruitment selection, Training & Development, Performance Management, Career planning and Management.' 
	POM.content4 = 'Directing: Individual and group behavior, motivation, motivation theories, motivational techniques, job satisfaction, job enrichment, leadership, types & theories of leadership, effective communication.'
	POM.content5 = 'Controlling: system and process of controlling, budgetary and non-budgetary control techniques, use of computers and IT in management control, productivity problems and management, control and performance, direct and preventive control, reporting.'



	BEE = subject()
	BEE.subject_name = 'BEE'
	BEE.pdf_link1 = 'BEE_unit1.pdf'
	BEE.pdf_link2 = 'BEE_unit2.pdf'
	BEE.pdf_link3 = 'BEE_unit3.pdf'
	BEE.pdf_link4 = 'BEE_unit4.pdf'
	BEE.pdf_link5 = 'BEE_unit5.pdf'

	BEE.content1 = 'DC Circuits Electrical circuit elements (R, L and C), voltage and current sources, Kirchoff current and voltage laws, analysis of simple circuits with dc excitation, Superposition, Thevenin and Norton Theorems, Time-domain analysis of firstorder RL and RC circuits.'
	BEE.content2 = 'AC Circuits Representation of sinusoidal waveforms, peak and rms values, phasor representation, real power, reactive power, apparent power, power factor, Analysis of single-phase ac circuits consisting of R, L, C, RL, RC, RLC combinations (series and parallel). Three phase balanced circuits, voltage and current relations in star and delta connections.'
	BEE.content3 = 'Transformers Construction, Working principle, EMF Equation, Ideal and Practical transformer, Equivalent circuit of Transformer, OC and SC tests on a transformer, Efficiency and Regulation, Auto transformer.'
	BEE.content4 = 'DC and AC Machines DC Generators: Construction, Principle of operation, EMF equation, Classification, Characteristics of shunt, series and compound generators. DC Motors: Classification, Torque equation, Characteristics, Efficiency, Speed Control of Series and Shunt Motors. Three - Phase Induction Motors: Construction, Principle of operation, Torque equation, torque-slip characteristics, Power stages, speed control of induction motors.'
	BEE.content5 = 'Electrical Installations Electrical Wiring: Types of wires and cables, Electrical Safety precautions in handling electrical appliances, electric shock, first aid for electric shock, safety rules. Components of LT Switchgear: Switch Fuse Unit (SFU), MCB, ELCB, MCCB, Earthing, Elementary calculations for energy consumption.'
	
	ES = subject()
	ES.subject_name = 'ES'
	ES.pdf_link1 = 'ES_unit1.pdf'
	ES.pdf_link2 = 'ES_unit2.pdf'
	ES.pdf_link3 = 'ES_unit3.pdf'
	ES.pdf_link4 = 'ES_unit4.pdf'
	ES.pdf_link5 = 'ES_unit5.pdf'

	ES.content1 = 'Environmental Studies: Definition, Scope and importance, need for public awareness. Natural resources: Use and over utilization of Natural Resources - Water resources, Food resources, Forest resources, Mineral resources, Energy resources, Land resources.'
	ES.content2 = 'Ecosystems: Concept of an ecosystem, structure and function of an ecosystem, role of producers, consumers and decomposers, energy flow in an ecosystem, food chains, food webs, ecological pyramids, Nutrient cycling, Bio-geo chemical cycles, Terrestrial and Aquatic ecosystems.'
	ES.content3 = 'Biodiversity: Genetic, species and ecosystem biodiversity, Bio-geographical classification of India, India as a Mega diversity nation. Values of biodiversity, hot-spots of biodiversity, threats to biodiversity, endangered and endemic species of India, methods of conservation of biodiversity.'
	ES.content4 = 'Environmental Pollution: Cause, effects and control measures of air pollution, water pollution, marine pollution, soil pollution, noise pollution and Solid waste management, nuclear hazards Environmental Legislations: Environment protection Act, Air, Water, Forest & Wild life Acts, issues involved in enforcement of environmental legislation, responsibilities of state and central pollution control boards.'
	ES.content5 = 'Social issues and the environment: Water conservation methods: Rain water harvesting and watershed management, Environmental ethics, Sustainable development and Climate change: Global warming, Ozone layer depletion, forest fires, and Contemporary issues.'
	
	sem3 = [DMA, DSA, BEE, BE, POM, ES]

	return render(request, 'elibrary/subjectview_sem3.html' ,{'sem3':sem3})

def subjectview_sem1(request): 
	ENG = subject()
	ENG.subject_name = 'ENG'
	ENG.pdf_link1 = 'Default.pdf'
	ENG.pdf_link2 = 'Default.pdf'
	ENG.pdf_link3 = 'Default.pdf'
	ENG.pdf_link4 = 'Default.pdf'
	ENG.pdf_link5 = 'Default.pdf'

	ENG.content1 = 'Understanding Communication in English: Introduction, nature and importance of communication; Process of communication; Types of communication - verbal and non-verbal; Barriers to communication; Intrapersonal and interpersonal communication; Understanding Johari Window. Vocabulary &Grammar: The concept of Word Formation; Use of appropriate prepositions and articles.'
	ENG.content2 = 'Developing Writing Skills I: Paragraph writing. – Structure and features of a paragraph; Cohesion and coherence. Rearranging jumbled sentences. Email and Mobile etiquette. Vocabulary & Grammar: Use of cohesive devices and correct punctuation.'
	ENG.content3 = 'Developing Writing Skills II: Précis Writing; Techniques of writing precisely. Letter Writing – Structure, format of a formal letter; Letter of request and the response Vocabulary and Grammar: Subject-verb agreement. Use of prefixes and suffixes to form derivatives. Avoiding redundancies.'
	ENG.content4 = 'Developing Writing Skills III: Report writing – Importance, structure, elements of style of formal reports ; Writing a formal report. Vocabulary and Grammar: Avoiding ambiguity - Misplaced modifiers. Use of synonyms and antonyms.'
	ENG.content5 = 'Developing Reading Skills: The reading process, purpose, different kinds of texts; Reading comprehension; Techniques of comprehension – skimming, scanning, drawing inferences and conclusions. Vocabulary and Grammar: Words often confused; Use of standard abbreviations.'



	OSP = subject()
	OSP.subject_name = 'OSP'
	OSP.pdf_link1 = 'Default.pdf'
	OSP.pdf_link2 = 'Default.pdf'
	OSP.pdf_link3 = 'Default.pdf'
	OSP.pdf_link4 = 'Default.pdf'
	OSP.pdf_link5 = 'Default.pdf'

	OSP.content1 = 'Wave Optics: Huygens’ principle –Superposition of waves –Interference of light by wave front splitting and amplitude splitting–Fresnel’s biprism – Interference in thin films in reflected light– Newton’s rings– Fraunhofer diffraction from a single slit –Double slit diffraction – Rayleigh criterion for limit of resolution– Concept of N-slits–Diffraction grating and its resolving power.'
	OSP.content2 = 'Lasers & Holography: Characteristics of lasers – Einstein’s coefficients –Amplification of light by population inversion –Different types of lasers: solid-state lasers: Ruby &Nd:YAG; gas lasers: He-Ne & CO2; semiconductor laser –Applications of lasers in engineering and medicine. Holography: Principle – Recording and reconstruction–Applications. Fiber Optics: Introduction –Construction –Principle –Propagation of light through an optical fiber – Numerical aperture and acceptance angle –Step-index and graded-index fibers –Pulse dispersion –Fiber losses–Fiber optic communication system –Applications.'
	OSP.content3 = 'Principles of Quantum Mechanics: Introduction –Wave nature of particles – de-Broglie hypothesis – Physical significance of ψ –Time-dependent and time-independent Schrodinger equations – Born interpretation – Probability current –Wave packets –Uncertainty principle –Particle in infinite square well potential –Scattering from potential step – Potential barrier and tunneling.'
	OSP.content4 = 'Band Theory of Solids: Salient features of free electron theory of metals (Classical and Quantum) – Fermi level –Density of states – Bloch’s theorem for particles in a periodic potential – Kronig-Penney model – Classification of solids: metals, semiconductors and insulators.'
	OSP.content5 = 'Semiconductors: Intrinsic and extrinsic semiconductors –Charge carrier concentration in intrinsic semiconductors –Dependence of Fermi level on carrier concentration and temperature in extrinsic semiconductors (qualitative) –Carrier generation and recombination –Carrier transport: diffusion and drift – P-N junction – Thermistor – Hall effect – LED –Solar cell.'



	PPS = subject()
	PPS.subject_name ='PPS'
	PPS.pdf_link1 = 'Default.pdf'
	PPS.pdf_link2 = 'Default.pdf'
	PPS.pdf_link3 = 'Default.pdf'
	PPS.pdf_link4 = 'Default.pdf'
	PPS.pdf_link5 = 'Default.pdf'

	PPS.content1 = 'Introduction to computers and Problem Solving: Components of a computer, Operating system, compilers, Program Development Environments, steps to solve problems, Algorithm, Flowchart / Pseudocode with examples. Introduction to programming: Programming languages and generations, categorization of high-level languages. Introduction to C: Introduction, structure of C program, keywords, identifiers, Variables, constants, I/O statements, operators, precedence, and associativity.'
	PPS.content2 = 'Introduction to decision control statements: Selective, looping, and nested statements. Functions: Introduction, uses of functions, Function definition, declaration, passing parameters to functions, recursion, scope of variables and storage classes, Case study using functions and control statements.'
	PPS.content3 = 'Arrays: Introduction, declaration of arrays, accessing and storage of array elements, 1-dimensional array, Searching (linear and binary search algorithms) and sorting (Selection and Bubble) algorithms, 2-D arrays, matrix operations. Strings: Introduction, strings representation, string operations with examples. Case study using arrays.'
	PPS.content4 = 'Pointers: Understanding computer’s memory, introduction to pointers, declaration pointer variables, pointer arithmetic, pointers and strings, array of pointers, dynamic memory allocation, advantages, and drawbacks of pointers. Structures: Structure definition, initialization and accessing the members of a structure, nested structures, structures and functions, self- referential structures, unions, and enumerated data types.'
	PPS.content5 = 'Files: Introduction to files, file operations, reading data from files, writing data to files, error handing during file operations. Preprocessor Directives: Types of preprocessor directives, examples.'

	M1 = subject()
	M1.subject_name = 'M1'
	M1.pdf_link1 = 'Default.pdf'
	M1.pdf_link2 = 'Default.pdf'
	M1.pdf_link3 = 'Default.pdf'
	M1.pdf_link4 = 'Default.pdf'
	M1.pdf_link5 = 'Default.pdf'

	M1.content1 = 'Matrices: Rank of a matrix, Echelon form, consistency of linear System of equations, Linear dependence of vectors, Eigen values, Eigenvectors, Properties of Eigen values, Cayley-Hamilton theorem, Quadratic forms, Reduction of quadratic form to canonical form by linear transformation, Nature of quadratic form.'
	M1.content3 = 'Partial Differentiation and Its Applications :Functions of two or more variables, Partial derivatives, Higher order partial derivatives, Total derivative, Differentiation of implicit functions, Jacobians, Taylor’s expansion of functions of two variables, Maxima and minima of functions of two variables.'
	M1.content4 = 'Vector Differential Calculus: Scalar and vector point functions, vector operator Del, Gradient, Directional derivative, Divergence, Curl, Del applied twice to point functions, Del applied to product of point functions (vector identities). Applications: Irrotational fields and Solenoidal fields.'
	M1.content5 = 'Vector Integral Calculus: Line integral, Surface integral and Volume integral. Green’s theorem in the plane, verifications of Stroke’s theorem (without proof) and Gauss’s divergence theorem (without proof).'

	
	sem1 = [ENG, OSP, PPS, M1]

	return render(request, 'elibrary/subjectview_sem1.html' ,{'sem1':sem1})

def subjectview_sem2(request): 
	M2 = subject()
	M2.subject_name = 'M2'
	M2.pdf_link1 = 'Default.pdf'
	M2.pdf_link2 = 'Default.pdf'
	M2.pdf_link3 = 'Default.pdf'
	M2.pdf_link4 = 'Default.pdf'
	M2.pdf_link5 = 'Default.pdf'

	M2.content1 = 'Differential Equations of First Order: Exact Differential Equations, Equations Reducible To Exact Equations, Linear Equations, Bernoulli’s Equations, Riccati’s and Clairaut’s Equations, Orthogonal trajectories.'
	M2.content2 = 'Higher Order Linear Differential Equations: Solutions of higher order linear equations with constants coefficients, Method of variation of parameters, solution of Cauchys homogeneous linear equation.applications: LR and LCRcircuits.'
	M2.content3 = 'Series Solutions of Differential Equations: Ordinary point, singular point and regular singular point, Series solution when x=a is an ordinary point of the equation. Legendre’s equation, Legendre’s Polynomial of first kind (without proof), Rodrigue’s formula, orthogonality of Legendre polynomials. Bessel’s equation, Bessel’s function of the first kind of order n (without proof), recurrence formulae for Jn(x) and related problems (i.eJ0(x), J1(x), J1/2(x), J-1/2(x), J3/2 (x), J-3/2(x)).'
	M2.content4 = 'Fourier Transorms: Fourier integral theorem (statement), Complex form of Fourier integrals. Fourier transforms, Inverse Fourier Transforms, Fourier Sine and Cosine transforms, Inverse Fourier Sine and Cosine Transforms. Properties of Fourier transforms: Linear property, change of scale property, shifting property and Modulation theorem.'
	M2.content5 = 'Z-Transforms: Definition, some standard Z-transforms, linearity property, damping rule, shifting Un to the right, shifting Un to the left, multiplication by ‘n’, initial and final value theorems. Inverse Z-Transform: evaluation of Inverse Z-transform by Convolution theorem, partial fractions method. Z- Transform application to difference equations.'



	CHEM = subject()
	CHEM.subject_name = 'CHEM'
	CHEM.pdf_link1 = 'Default.pdf'
	CHEM.pdf_link2 = 'Default.pdf'
	CHEM.pdf_link3 = 'Default.pdf'
	CHEM.pdf_link4 = 'Default.pdf'
	CHEM.pdf_link5 = 'Default.pdf'

	CHEM.content1 = 'Atomic and molecular structure and Chemical Kinetics: Atomic and molecular structure: Molecular Orbital theory - atomic and molecular orbitals. Linear combination of atomic orbitals (LCAO) method. Molecular orbitals of diatomic molecules. Molecular Orbital Energy level diagrams (MOED) of diatomic molecules & molecular ions (H2 , He2+,N2 , O2 , O2 ¯ , CO, NO). Pi- molecular orbitals of benzene and its aromaticity. Chemical Kinetics: Introduction, Terms involved in kinetics: rate of reaction, order & molecularity; First order reaction-Characteristics: units of first order rate constant & its half-life period, second order reactionCharacteristics: units of second order rate constant & its half- life period. Numericals.'
	CHEM.content2 = 'Use of free energy in chemical equilibria Use of free energy in chemical equilibria: Thermodynamic functions: Internal energy, entropy and free energy. Significance of entropy and free energy (criteria of spontaneity). Free energy and emf (Gibbs Helmholtz equations and its applications). Cell potentials, electrode potentials, – Reference electrodes (NHE, SCE)- electrochemical series. Nernst equation and its applications. Determination of pH using combined Glass & Calomel electrode. Potentiometric Acid base & Redox Titrations. Numericals.' 
	CHEM.content3 = 'Stereochemistry: Representations of 3 dimensional structures, Types of stereoisomerism- Conformational isomerism – confirmations of n-butane (Newman and sawhorse representations), Configurational isomerism - Geometrical (cis-trans) isomerism & Optical isomerism- optical activity, Symmetry and chirality: Enantiomers (lactic acid) & Diastereomers (Tartaric acid), Absolute configurations, Sequence rules for R&S notation.'
	CHEM.content4 = 'Hardness of water – Types, units of hardness, Disadvantages of hard water, Alkalinity and Estimation of Alkalinity of water, Boiler troubles - scales & sludge formation, causes and effects, Softening of water by lime soda process (Cold lime soda process),ion exchange method and Reverse Osmosis. Specifications of potable water & industrial water. Disinfection of water by Chlorination; break point chlorination, BOD and COD definition, Estimation (only brief procedure) and significance, Numericals'
	CHEM.content5 = 'Introduction, Terms used in polymer science; Thermoplastic polymers (PVC) &Thermosetting polymers (Bakelite); Elastomers (Natural rubber). Conducting polymers- Definition, classification and applications. Polymers for Electronics: Polymer resists for integrated circuit fabrication, lithography and photolithography.'

	OOPS = subject()
	OOPS.subject_name = 'OOPS'
	OOPS.pdf_link1 = 'Default.pdf'
	OOPS.pdf_link2 = 'Default.pdf'
	OOPS.pdf_link3 = 'Default.pdf'
	OOPS.pdf_link4 = 'Default.pdf'
	OOPS.pdf_link5 = 'Default.pdf'

	OOPS.content1 = 'Introduction to Object Oriented Programming (OOP): Computer Programming and Programming Languages, Features of Object Oriented Programming, Merits and Demerits of Object, Applications of Object Oriented Programming, Differences between Popular Programming Languages'
	OOPS.content2 = 'Decision Control Statements: Introduction to Decision Control Statements, Selection/Conditional Branching Statements, Basic Loop Structures/ Iterative Statements, Nested Loops, The break Statement, The continue Statement, The pass Statement, The else Statement used with Loops'
	OOPS.content3 = 'Classes and Objects: Introduction, Classes and Objects, init method, Class variables, and Object variables, Public and Private Data members, calling methods from other methods, built-in class attributes, garbage collection, class methods, static methods'
	OOPS.content4 = 'Inheritance: Introduction, Inheriting classes, Types of Inheritance, Composition or Containership or complex objects, Abstract classes and interfaces.'
	OOPS.content5 = 'Error and Exception Handling: Introduction to errors and exceptions, Handling Exceptions, Multiple Except Blocks, Multiple Exceptions in a Single Block, Except Block Without Exception, The else Clause, Raising Exceptions, Instantiating Exceptions, Handling Exceptions in Invoked Functions, Built-in and User-defined Exceptions, The finally Block, Pre-defined Clean–up Action, Re-raising Exception, Assertions in Python GUI Programming with tkinter package'



	DE = subject()
	DE.subject_name = 'DE'
	DE.pdf_link1 = 'Default.pdf'
	DE.pdf_link2 = 'Default.pdf'
	DE.pdf_link3 = 'Default.pdf'
	DE.pdf_link4 = 'Default.pdf'
	DE.pdf_link5 = 'Default.pdf'

	DE.content1 = 'Differential Equations of First Order: Exact Differential Equations, Equations Reducible To Exact Equations, Linear Equations, Bernoulli’s Equations, Riccati’s and Clairaut’s Equations, Orthogonal trajectories.'
	DE.content2 = 'Higher Order Linear Differential Equations: Solutions of higher order linear equations with constants coefficients, Method of variation of parameters, solution of Cauchys homogeneous linear equation.applications: LR and LCRcircuits.'
	DE.content3 = 'Series Solutions of Differential Equations: Ordinary point, singular point and regular singular point, Series solution when x=a is an ordinary point of the equation. Legendre’s equation, Legendre’s Polynomial of first kind (without proof), Rodrigue’s formula, orthogonality of Legendre polynomials. Bessel’s equation, Bessel’s function of the first kind of order n (without proof), recurrence formulae for Jn(x) and related problems (i.eJ0(x), J1(x), J1/2(x), J-1/2(x), J3/2 (x), J-3/2(x)).'
	DE.content4 = 'Fourier Transorms: Fourier integral theorem (statement), Complex form of Fourier integrals. Fourier transforms, Inverse Fourier Transforms, Fourier Sine and Cosine transforms, Inverse Fourier Sine and Cosine Transforms. Properties of Fourier transforms: Linear property, change of scale property, shifting property and Modulation theorem.'
	DE.content5 = 'Z-Transforms: Definition, some standard Z-transforms, linearity property, damping rule, shifting Un to the right, shifting Un to the left, multiplication by ‘n’, initial and final value theorems. Inverse Z-Transform: evaluation of Inverse Z-transform by Convolution theorem, partial fractions method. Z- Transform application to difference equations.'
	
	sem2 = [M2, CHEM, OOPS, DE]

	return render(request, 'elibrary/subjectview_sem2.html' ,{'sem2':sem2})


def subjectview_sem4(request): 
	DLCA = subject()
	DLCA.subject_name = 'DLCA'
	DLCA.pdf_link1 = 'Default.pdf'
	DLCA.pdf_link2 = 'Default.pdf'
	DLCA.pdf_link3 = 'Default.pdf'
	DLCA.pdf_link4 = 'Default.pdf'
	DLCA.pdf_link5 = 'Default.pdf'

	DLCA.content1 = 'Digital Logic Circuits : Digital Computers, Logic Gates, Boolean Algebra, Map simplification, Product –of-sums Simplification, Don’t –Care Conditions, Combinational Circuits , Half-Adder, Full –Adder, Flip-Flops: SR,D,JK,T FlipFlops, Edge triggered Flip-Flops, Excitation Tables, Digital Components: Integrated circuits, Decoders. Encoders, Multiplexers.'
	DLCA.content2 = 'Registers: Register with Parallel load, Shift Register, Counters. Data Representation: Data Types, Number Systems, Octal and Hexadecimal Numbers, Decimal Representation, Alphanumeric Representation, Complements: (r-1)’s Complement, r’s Complement, Subtraction of Unsigned Numbers, Fixed–Point Representation, Floating –Point Representation, Other Binary Codes, Error Detection Codes.'
	DLCA.content3 = 'Central Processing Unit: General register Organization, Stack Organization: Register Stack, Memory Stack, Reverse Polish Notation, Instruction Formats: ThreeAddress Instructions, Two-Address Instructions, One-Address Instructions, Zero-Address Instructions, RISC Instructions, Addressing Modes, Data Transfer and Manipulation, Program Control, Reduced Instruction Set Computer (RISC): CISC Characteristics, RISC Characteristics'
	DLCA.content4 = 'Input-Output Organization: Peripheral Devices: ASCII AlphanumericCharacters, Input-output Interface: I/O Bus and Interface Modules, Asynchronous Data Transfer: Strobe Control, Handshaking, Asynchronous Communication Interface, First-In- First-Out Buffer, Modes of Transfer: Interrupt-Initiated I/O, Priority Interrupt: Daisy Chaining Priority, Parallel Priority Interrupt, Priority Encoder, Direct Memory Access (DMA): DMA Controller.'
	DLCA.content5 = 'Memory Organization: Memory Hierarchy, Main Memory: RAM and ROM Chips, Memory Address Map, Memory Connection to CPU, Auxiliary memory: Magnetic Disks, Magnetic Tapes, Associative Memory: Hardware Organization, Match Logic, Read and Write Operations, Cache Memory: Associative Mapping, Direct Mapping, Set-Associative Mapping, Virtual Memory: Address Space and Memory Space, Address Mapping using Pages, Associative Memory Page Table, Page Replacement.'
	


	DBMS = subject()
	DBMS.subject_name = 'DBMS'
	DBMS.pdf_link1 = 'Default.pdf'
	DBMS.pdf_link2 = 'Default.pdf'
	DBMS.pdf_link3 = 'Default.pdf'
	DBMS.pdf_link4 = 'Default.pdf'
	DBMS.pdf_link5 = 'Default.pdf'

	DBMS.content1 = 'Introduction: Database-System Applications, Purpose of Database Systems, View of Data, Database Languages, Relational Databases, Database Design, Data Storage and Querying, Transaction Management, Database Architecture, Data Mining and Information Retrieval Specialty Databases, Database Users and Administrators.'
	DBMS.content2 = 'Introduction to the Relational Model: Structure of Relational Databases, Database Schema, Keys, Schema Diagrams, Relational Query Languages, Relational Operations.'
	DBMS.content3 = 'Advanced SQL: Accessing SQL from a Programming Language, Functions and Procedures, Triggers, Recursive Queries, Advanced Aggregation Features.'
	DBMS.content4 = 'Indexing and Hashing: Basic Concepts, Ordered Indices, B+ Tree Index Files, Multiple-Key Access, Static Hashing, Dynamic Hashing, Comparison of Ordered Indexing and Hashing, Bitmap Indices, Index Definition in SQL Transactions: Transaction Concept, a Simple Transaction Model, Transaction Atomicity and Durability, Transaction Isolation, Serializability, Transaction Isolation and Atomicity, Transaction Isolation Levels.'
	DBMS.content5 = 'Concurrency Control: Lock-Based Protocols, Deadlock Handling, Multiple Granularity, Timestamp-Based Protocols, Validation-Based Protocols, Multiversion Schemes, Snapshot Isolation, Insert Operations, Delete Operations and Predicate Reads.'



	JP = subject()
	JP.subject_name = 'JP'
	JP.pdf_link1 = 'Default.pdf'
	JP.pdf_link2 = 'Default.pdf'
	JP.pdf_link3 = 'Default.pdf'
	JP.pdf_link4 = 'Default.pdf'
	JP.pdf_link5 = 'Default.pdf'

	JP.content1 = 'Introduction to Java: Objects, Classes, structure a java program, difference betweenjdk and jre, Java Primitive Types, Basic Operators, Conditional and Logical statements.'
	JP.content2 = 'Inheritance, Interfaces and Packages in Java: Defining super / sub classes, Abstract classes, Method overriding, Interfacesand new features in latest version. Packages: Defining, Creatingand Accessing a Package, importing packages.'
	JP.content3 = 'Exception Handling in Java: What are exceptions, Error vs. Exception, usage of try, catch, throw throws and finally clauses, writing your own exception classes, Difference between checked vs. unchecked Exceptions.'
	JP.content4 = 'Collections: Overview of Java Collection Framework, Collection Interfaces – Collection, Set, List, Map, Commonly used Collectionclasses – ArrayList, LinkedList, HashSet, TreeSet, HashMap, TreeMap, legacy and class, Iteration over Collections – Iterator and ListIterator, Enumeration interfaces, differentiate Comparable and Comparator'
	JP.content5 = 'GUI Design & Event Handling: Component, Container, Color,GUI Controls, Layout Managers, Introduction to Swings, Delegation Event Model, Event Classes, Source of Events, Event Listener Interfaces. Handlingbutton click, mouse and keyboard events, and Adapter classes. Writing GUI Based applications, Applets, life cycle of an Applet, Developing and running applets, passing parametersto applets'



	DAA = subject()
	DAA.subject_name = 'DAA'
	DAA.pdf_link1 = 'Default.pdf'
	DAA.pdf_link2 = 'Default.pdf'
	DAA.pdf_link3 = 'Default.pdf'
	DAA.pdf_link4 = 'Default.pdf'
	DAA.pdf_link5 = 'Default.pdf'

	DAA.content1 = 'Introduction: Algorithm Specification, Performance analysis: Space Complexity, Time Complexity, Asymptotic Notation (O, Omega, Theta), Practical Complexities, Performance Measurement, Elementary Data Structures: Stacks and Queues, Trees, Dictionaries , Priority Queues, Sets and Disjoint Set Union'
	DAA.content2 = 'Divide and Conquer: The general method, Finding the Maximum and Minimum, Merge Sort, Quick Sort, Selection Sort, Strassen’s Matrix Multiplication.'
	DAA.content3 = 'Dynamic Programming: The General Method, Multistage graphs, All Pair Shortest Paths, Single Source Shortest Paths, Optimal Binary Search Trees, 0/1 Knapsack, Reliability Design, The Traveling Salesperson Problem.'
	DAA.content4 = 'Backtracking: The General Method, 8-Queens Problem, Graph Colouring, Hamilton cycles, Knapsack Problem.'
	DAA.content5 = 'NP-Hard and NP-Complete Problems: Basic Concepts: Non-Deterministic Algorithms, the Classes NP Hard and NP Complete. Cook’s theorem, NP-Hard Graph Problems: Node Cover Decision Problem, Chromatic Number Decision Problem, Directed Hamiltonian Cycle, Traveling Salesperson Decision Problem, NP Hard Scheduling Problems: Job Shop Scheduling.'

	IC = subject()
	IC.subject_name = 'IC'
	IC.pdf_link1 = 'Default.pdf'
	IC.pdf_link2 = 'Default.pdf'
	IC.pdf_link3 = 'Default.pdf'
	IC.pdf_link4 = 'Default.pdf'
	IC.pdf_link5 = 'Default.pdf'

	IC.content1 = 'Constitution of India: Introduction and salient features, Constitutional history. Directive Principles of State Policy - Its importance and implementation.'
	IC.content2 = 'Union Government and its Administration:Structure of the Indian Union: Federalism, distribution of legislative and financial powers between the Union and the States. Parliamentary form of government in India. President: role, power and position'
	IC.content3 = 'Emergency Provisions in India: National emergency, President rule, Financial emergency'
	IC.content4 = 'Local Self Government:District’s Administration Head: Role and Importance. Municipalities: Introduction, Mayor and role of Elected Representative, CEO of Municipal Corporation.'
	IC.content5 = 'Scheme of The Fundamental Rights & Duties: Fundamental Duties - The legal status. Scheme of The Fundamental Rights - To Equality, to certain Freedom Under Article 19, to Life And Personal Liberty Under Article 21.'
	sem4 = [DLCA, DBMS, JP, DAA, IC]


	return render(request, 'elibrary/subjectview_sem4.html' ,{'sem4':sem4})

def subjectview_sem5(request): 
	OS = subject()
	OS.subject_name = 'OS'
	OS.pdf_link1 = 'Default.pdf'
	OS.pdf_link2 = 'Default.pdf'
	OS.pdf_link3 = 'Default.pdf'
	OS.pdf_link4 = 'Default.pdf'
	OS.pdf_link5 = 'Default.pdf'

	OS.content1 = 'Introduction: Definition of Operating System, Computer-System Organization, Computer-System Architecture, Operating-System Structure, Operating-System Operations, Process Management, Memory Management, Storage Management, Protection and Security, Computing Environments, Open-Source Operating Systems.'
	OS.content2 = 'Process Scheduling: Basic Concepts, Scheduling Criteria, Scheduling Algorithms, Thread Scheduling, Multiple-Processor Scheduling. Synchronization: Background, The Critical-Section Problem, Peterson‘s Solution, Synchronization Hardware, Mutex Locks, Semaphores, Classic Problems of Synchronization, Monitors.'
	OS.content3 = 'Memory Management Straegies: Background, Swapping, Contiguous Memory Allocation, Segmentation, Paging, Structure of the Page Table. Virtual Memory Management: Background, Demand Paging, Copy-on-Write, Page Replacement, Allocation of Frames, Thrashing, Memory-Mapped Files, Allocating Kernel Memory.'
	OS.content4 = 'File-System: File Concept, Access Methods, Directory and Disk Structure, File-System Mounting, File Sharing Protection. Implementing File Systems: File-System Structure, File-System Implementation, Directory Implementation, Allocation Methods, Free-Space Management, Efficiency and Performance. '
	OS.content5 = 'System Protection: Goals of Protection, Principles of Protection, Domain of Protection, Access Matrix, Implementation of the Access Matrix, Access Control, Revocation of Access Rights, Capability-Based Systems'


	
	TA = subject()
	TA.subject_name = 'TA'
	TA.pdf_link1 = 'Default.pdf'
	TA.pdf_link2 = 'Default.pdf'
	TA.pdf_link3 = 'Default.pdf'
	TA.pdf_link4 = 'Default.pdf'
	TA.pdf_link5 = 'Default.pdf'

	TA.content1 = 'Automata: Introduction to Finite Automata, the Central Concepts of Automata Theory: Alphabets, Strings and Languages.'
	TA.content2 = 'Regular Expression and languages: Regular Expressions: The Operators of Regular Expressions, Building Regular Expressions. Finite Automata and Regular Expression: From DFAs to Regular Expressions, Converting DFA‘s to Regular Expressions by Eliminating States, Converting Regular Expressions to Automata, Applications of Regular Expressions, Algebraic Laws for Regular Expressions.'
	TA.content3 = 'Context Free Grammars and Languages: Context-Free Grammars: Definition of Context Free Grammars, Derivations using a Grammar, Leftmost and Rightmost Derivation, The language of a Grammar, Parse Trees: Constructing Parse Trees, The Yield of a Parse Tree, Applications of CFGs, Ambiguity in Grammars and Languages: Ambiguous Grammars, Removing Ambiguity From Grammars, Leftmost Derivations as way to Express Ambiguity, Inherent Ambiguity.'
	TA.content4 = 'Pushdown Automata: Definition of pushdown automaton: The Formal Definition of PDA, Graphical Notation for PDA‘s, Instantaneous Description of a PDA, The Language of a PDA.'
	TA.content5 = 'Introduction to Turing Machines: Problems that Computer Cannot Solve: The Turing Machine: Notation for the TM, Instantaneous Descriptions for TM‘s, Transitions Diagrams, The Language of a TM, Turing Machines and Halting, Programming Techniques for Turing Machines: Storage in the State, Multiple Tracks, Subroutines.'
    
	sem5 = [OS, TA]

	return render(request, 'elibrary/subjectview_sem5.html' ,{'sem5':sem5})


def subjectview_sem6(request): 
	AI = subject()
	AI.subject_name = 'AI'
	AI.pdf_link1 = 'Default.pdf'
	AI.pdf_link2 = 'Default.pdf'
	AI.pdf_link3 = 'Default.pdf'
	AI.pdf_link4 = 'Default.pdf'
	AI.pdf_link5 = 'Default.pdf'

	AI.content1 ='Introduction: The Foundations of AI, History of AI. Intelligent agents – Agents and Environments, Good Behavior: The Concept of Rationality, The Nature of Environments, The Structure of Agents.'
	AI.content2 ='Logic Concepts and Logic Programming: Introduction, Propositional Calculus, Propositional Logic, Natural Deduction System, Axiomatic System, Semantic Tableau System in Propositional Logic, Resolution Refutation in Propositional Logic, Predicate Logic, Logic Programming.'
	AI.content3 ='Quantifying Uncertainty: Acting under Uncertainty, Basic Probability Notation, Inference Using Full JointDistributions, Independence, Bayes‘ Rule and its Use. '
	AI.content4 ='Learning from Examples: Forms of Learning, Supervised Learning, Learning Decision Trees, Evaluating and Choosing the Best Hypothesis, The Theory of Learning, Regression and Classification with Linear Models, Artificial Neural Networks, Nonparametric Models, Support Vector Machines. '
	AI.content5 ='Natural Language Processing: Language Models, Text Classification, Information Retrieval, Information Extraction.'



	IS = subject()
	IS.subject_name = 'IS'
	IS.pdf_link1 = 'Default.pdf'
	IS.pdf_link2 = 'Default.pdf'
	IS.pdf_link3 = 'Default.pdf'
	IS.pdf_link4 = 'Default.pdf'
	IS.pdf_link5 = 'Default.pdf'

	IS.content1 = 'Introduction to Information Security: History of Information Security, What Is Security, CNSS security model, Components of an Information System, Balancing Information Security and Access, Approaches to Information Security Implementation, Security in the Systems Life Cycle, Security Professionals and the Organization.'
	IS.content2 = 'Risk management: An Overview of Risk Management, Risk Identification, Risk assessment, Risk Control, Quantatitive versus Qualitative Risk Management Practices, Recommended Risk Control Practices.'
	IS.content3 = 'Cryptography: Introduction, Foundations of Cryptology, Cipher methods, cryptographic Algorithms, Cryptographic Tools, Protocols for Secure Communications.'
	IS.content4 = 'Electronic Mail Security: Pretty Good Privacy, S/MIME, DomainKeys Identified Mail.'
	IS.content5 = 'Information security Maintenance: Introduction, Security Management Maintenance Models, Digital Forensics.'
	sem6 = [AI, IS]

	return render(request, 'elibrary/subjectview_sem6.html' ,{'sem6':sem6})



def subjectview_sem7(request): 
	DS = subject()
	DS.subject_name = 'DS'
	DS.pdf_link1 = 'Default.pdf'
	DS.pdf_link2 = 'Default.pdf'
	DS.pdf_link3 = 'Default.pdf'
	DS.pdf_link4 = 'Default.pdf'
	DS.pdf_link5 = 'Default.pdf'

	DS.content1 = 'Introduction: Definition of A Distributed System; Goals- Making Resources Accessible, Distribution Transparency, Openness, Scalability; Types of Distributed Systems- Distributed Computing Systems, Distributed Information Systems, Distributed Pervasive Systems.'
	DS.content2 = 'Processes: Threads - Introduction to Threads, Threads in Distributed Systems; Virtualization - The Role of Virtualization In Distributed Systems, Architectures of Virtual Machines; Clients- Networked User Interfaces, Client-Side Software for Distribution Transparency; Servers- General Design Issues, Server Clusters, Managing Server Clusters; Code Migration- Approaches to Code Migration, Migration and Local Resources, Migration in Heterogeneous Systems.'
	DS.content3 = 'Naming: Names, Identifiers, and Addresses; Flat Naming- Simple Solutions, Home-Based Approaches, Distributed Hash Tables, Hierarchical Approaches; Structured Naming- Name Spaces, Name Resolution, the Implementation of a Name Space; Attribute-based Naming- Directory Services, Hierarchical Implementations: LDAP, Decentralized Implementations.'
	DS.content4 = 'Consistency And Replication: Introduction- Reasons for Replication, Replication as Scaling Technique; Data-Centric Consistency Models- Continuous Consistency, Consistent Ordering of Operations.'
	DS.content5 = 'Distributed Object-Based Systems: Architecture- Distributed Objects, Example: Enterprise Java Beans, Example- Globe Distributed Shared Objects; ProcessesObject Servers, Example: The Ice Runtime System; Communication- Binding a Client to an Object, Static versus Dynamic Remote Method Invocations.'
	


	BDA = subject()
	BDA.subject_name = 'BDA'
	BDA.pdf_link1 = 'Default.pdf'
	BDA.pdf_link2 = 'Default.pdf'
	BDA.pdf_link3 = 'Default.pdf'
	BDA.pdf_link4 = 'Default.pdf'
	BDA.pdf_link5 = 'Default.pdf'

	BDA.content1 = 'Introduction to Big Data: Importance of Big Data, when to considerBig Data as a solution, Big Data use cases: IT for IT Log Analytics, the Fraud Detection Pattern, and Social Media Pattern.'
	BDA.content2 = 'MapReduce: What is Map reduce, Architecture of map reduce.How MapReduce Works: Anatomy of a MapReduce Job Run, Job Submission, Job Initialization, Task Assignment, Task Execution, Progress and Status Updates, Job Completion.'
	BDA.content3 = 'No SQL Databases: Review of traditional Databases, Need for NoSQL Databases, Columnar Databases, Failover and reliability principles, CAP Theorem, Differences between SQL and NoSQL databases.'
	BDA.content4 = 'Pig: Installing and Running Pig, an Example, Generating Examples, Comparison with Databases, Pig Latin, User-Defined Functions, Data Processing Operators, Pig in Practice'
	BDA.content5 = 'Spark:Importance of Spark Framework, Components of the Spark unified stack, Batch and Real-Time Analytics with Apache Spark, Resilient Distributed Dataset (RDD), SCALA (Object Oriented and Functional Programming).'
	sem7 = [DS, BDA]

	return render(request, 'elibrary/subjectview_sem7.html' ,{'sem7':sem7})


def subjectview_sem8(request): 
	M1 = subject()
	


	PPS = subject()

		
	sem8 = [PPS, M1]

	return render(request, 'elibrary/subjectview_sem8.html' ,{'sem8':sem8})


def home(request):
	return render(request,'elibrary/home.html')

@login_required
def it_sems(request):
	return render(request,'elibrary/it_sems.html') 

@login_required
def cse_sems(request):
	return render(request,'elibrary/cse_sems.html') 

@login_required
def ece_sems(request):
	return render(request,'elibrary/ece_sems.html') 

def eee_sems(request):
	return render(request,'elibrary/eee_sems.html')

def it_sem1(request):
	return render(request,'elibrary/it_sem1.html') 

def it_sem2(request):
	return render(request,'elibrary/it_sem2.html')  

def it_sem3(request):
	return render(request,'elibrary/it_sem3.html') 

def it_sem4(request):
	return render(request,'elibrary/it_sem4.html') 

def it_sem5(request):
	return render(request,'elibrary/it_sem5.html') 

def it_sem6(request):
	return render(request,'elibrary/it_sem6.html') 

def it_sem7(request):
	return render(request,'elibrary/it_sem7.html') 

def it_sem3_DMA(request):
	return render(request,'elibrary/it_sem3_DMA.html')

def cse_sem1(request):
	return render(request,'elibrary/cse_sem1.html') 

def cse_sem2(request):
	return render(request,'elibrary/cse_sem2.html')  

def cse_sem3(request):
	return render(request,'elibrary/cse_sem3.html') 

def cse_sem4(request):
	return render(request,'elibrary/cse_sem4.html') 

def cse_sem5(request):
	return render(request,'elibrary/cse_sem5.html')  

def cse_sem6(request):
	return render(request,'elibrary/cse_sem6.html') 

def cse_sem7(request):
	return render(request,'elibrary/cse_sem7.html') 

def ece_sem1(request):
	return render(request,'elibrary/ece_sem1.html') 

def ece_sem2(request):
	return render(request,'elibrary/ece_sem2.html')  

def ece_sem3(request):
	return render(request,'elibrary/ece_sem3.html') 

def ece_sem4(request):
	return render(request,'elibrary/ece_sem4.html') 

def ece_sem5(request):
	return render(request,'elibrary/ece_sem5.html')  

def ece_sem6(request):
	return render(request,'elibrary/ece_sem6.html') 

def ece_sem7(request):
	return render(request,'elibrary/ece_sem7.html') 

@login_required
def stack_home(request):
    if 'q' in request.GET:
        q=request.GET['q']
        quests=Question.objects.annotate(total_comments=Count('answer__comment')).filter(title__icontains=q).order_by('-id')
    else:
        quests=Question.objects.annotate(total_comments=Count('answer__comment')).all().order_by('-id')
    paginator=Paginator(quests,5)
    page_num = request.GET.get('page',1)
    quests=paginator.page(page_num)
    return render(request,'elibrary/home2.html',{'quests':quests})


class UserQuestionsListView(ListView):
	model = Question
	template_name = "elibrary/user-qstns.html"
	context_object_name = "Question"
	paginate_by = 5

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Question.objects.filter(user=user).order_by('-id')

class QuestionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Question
	fields = ['title','detail','tags']

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

	def test_func(self):
		question = self.get_object()
		if self.request.user == question.author:
			return True
		else:
			return False

def detail(request,id):
    quest=Question.objects.get(pk=id)
    tags=quest.tags.split(',')
    answers=Answer.objects.filter(question=quest)
    answerform=AnswerForm
    if request.method=='POST':
        answerData=AnswerForm(request.POST)
        if answerData.is_valid:
            answer=answerData.save(commit=False)
            answer.question=quest
            answer.user=request.user
            answer.save()
            messages.success(request,'Answer has been submitted!')
    return render(request,'elibrary/detail.html',{
		'id':id,
        'quest':quest,
        'tags':tags,
        'answers':answers,
        'answerform':answerform,
    })


def save_comment(request):
    if request.method=='POST':
        comment=request.POST['comment']
        answerid=request.POST['answerid']
        answer=Answer.objects.get(pk=answerid)
        user=request.user
        Comment.objects.create(
            answer=answer,
            comment=comment,
            user=user
        )
        return JsonResponse({'bool':True})

def save_upvote(request):
    if request.method=='POST':
        answerid=request.POST['answerid']
        answer=Answer.objects.get(pk=answerid)
        user=request.user
        check=UpVote.objects.filter(answer=answer,user=user).count()
        if check > 0:
            return JsonResponse({'bool':False})
        else:
            UpVote.objects.create(
                answer=answer,
                user=user
            )
        return JsonResponse({'bool':True})

def save_downvote(request):
    if request.method=='POST':
        answerid=request.POST['answerid']
        answer=Answer.objects.get(pk=answerid)
        user=request.user
        check=DownVote.objects.filter(answer=answer,user=user).count()
        if check > 0:
            return JsonResponse({'bool':False})
        else:
            DownVote.objects.create(
                answer=answer,
                user=user
            )
        return JsonResponse({'bool':True})

def ask_form(request):
    form=QuestionForm
    if request.method=='POST':
        questForm=QuestionForm(request.POST)
        if questForm.is_valid():
            questForm=questForm.save(commit=False)
            questForm.user=request.user
            questForm.save()
            messages.success(request,'Question has been added.')
    return render(request,'elibrary/ask-question.html',{'form':form})



def tag(request,tag):
    quests=Question.objects.annotate(total_comments=Count('answer__comment')).filter(tags__icontains=tag).order_by('-id')
    paginator=Paginator(quests,5)
    page_num=request.GET.get('page',1)
    quests=paginator.page(page_num)
    return render(request,'elibrary/tag.html',{'quests':quests,'tag':tag})

def profile(request):
    quests=Question.objects.filter(user=request.user).order_by('-id')
    answers=Answer.objects.filter(user=request.user).order_by('-id')
    comments=Comment.objects.filter(user=request.user).order_by('-id')
    upvotes=UpVote.objects.filter(user=request.user).order_by('-id')
    downvotes=DownVote.objects.filter(user=request.user).order_by('-id')
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile has been modified!')
            return redirect('/profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    return render(request,'elibrary/profile.html',{
        'u_form':u_form,
        'p_form':p_form,
        'quests':quests,
        'answers':answers,
        'comments':comments,
        'upvotes':upvotes,
        'downvotes':downvotes,
    })


def tags(request):
    quests=Question.objects.all()
    tags=[]
    for quest in quests:
        qtags=[tag.strip() for tag in quest.tags.split(',')]
        for tag in qtags:
            if tag not in tags:
                tags.append(tag)
    # Fetch Questions
    tag_with_count=[]
    for tag in tags:
        tag_data={
            'name':tag,
            'count':Question.objects.filter(tags__icontains=tag).count()
        }
        tag_with_count.append(tag_data)
    return render(request,'elibrary/tags.html',{'tags':tag_with_count})
        
        