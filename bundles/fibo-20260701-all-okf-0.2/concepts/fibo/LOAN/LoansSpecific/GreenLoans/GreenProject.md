---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: green project
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: project that contributes to environmental sustainability by addressing climate change, conserving natural resources,
      reducing pollution, or promoting ecological balance
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#example
    value: 'Examples include: renewable energy projects (e.g., solar, wind, hydroelectric power), green buildings certified
      by recognized standards (e.g., LEED, BREEAM), sustainable water and wastewater management systems, pollution reduction
      technologies and systems, sustainable forestry and agriculture initiatives, circular economy projects, such as recycling
      or waste-to-energy facilities, low-carbon transportation infrastructure (e.g., electric vehicle charging stations, public
      transit projects), and the like.'
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: Loan Market Association (LMA) Green Loan Principles, available at https://www.icmagroup.org/assets/documents/Regulatory/Green-Bonds/LMA_Green_Loan_Principles_Booklet-220318.pdf.
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.prince2.com/usa/blog/project-vs-programme
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.lma.eu.com/application/files/8916/9755/2443/Green_Loan_Principles_23_February_2023.pdf
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Green projects must align with established green finance principles, such as the Green Loan Principles (GLP) issued
      by the Loan Market Association (LMA), or other recognized sustainability frameworks.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The borrower must demonstrate that the project meets predefined eligibility criteria for green financing. These
      criteria are usually aligned with the taxonomy or standards set forth by the Green Loan Principles, the EU Taxonomy
      for Sustainable Activities, or other regional or international guidelines.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'To qualify as a green project within a green loan: (a) the project must meet use-of-proceeds requirements, meaning
      that funds must be exclusively allocated to activities that qualify as green, (b) the borrower must establish clear
      processes for evaluating and selecting eligible projects, (c) there must be transparency in how funds are managed and
      allocated, often verified through audits or certifications, and (d) the borrower must report regularly on the environmental
      impact of the project, typically through measurable metrics (e.g., tons of CO₂ avoided, energy saved).'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/GreenProjectUseOfProceedsProvision
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RegulatoryAgencies/isGovernedBy
  subclass_of:
  - concept: /concepts/fibo/LOAN/LoansSpecific/GreenLoans/EnvironmentalProject.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/EnvironmentalProject
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/GreenProject
sources:
- id: fibo-source-cff1f078be
  resource: references/fibo/LOAN/LoansSpecific/GreenLoans.rdf
  sha256: cff1f078bed4eeb9970073ab5ccbace470a24c6150ac1e18310cbe1894b9e006
  title: FIBO source LOAN/LoansSpecific/GreenLoans.rdf
title: green project
type: Ontology Class
---

# green project

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/GreenLoans/GreenProject>

## Definition

project that contributes to environmental sustainability by addressing climate change, conserving natural resources, reducing pollution, or promoting ecological balance

## Relationships

- **Subclass of**: [EnvironmentalProject](/concepts/fibo/LOAN/LoansSpecific/GreenLoans/EnvironmentalProject.md)

## Constraints

- **[isGovernedBy](<https://www.omg.org/spec/Commons/RegulatoryAgencies/isGovernedBy>)**: some values from of type [GreenProjectUseOfProceedsProvision](/concepts/fibo/LOAN/LoansSpecific/GreenLoans/GreenProjectUseOfProceedsProvision.md)

## Annotations

- **label**: green project
- **definition**: project that contributes to environmental sustainability by addressing climate change, conserving natural resources, reducing pollution, or promoting ecological balance
- **example** (en): Examples include: renewable energy projects (e.g., solar, wind, hydroelectric power), green buildings certified by recognized standards (e.g., LEED, BREEAM), sustainable water and wastewater management systems, pollution reduction technologies and systems, sustainable forestry and agriculture initiatives, circular economy projects, such as recycling or waste-to-energy facilities, low-carbon transportation infrastructure (e.g., electric vehicle charging stations, public transit projects), and the like.
- **adaptedFrom**: Loan Market Association (LMA) Green Loan Principles, available at https://www.icmagroup.org/assets/documents/Regulatory/Green-Bonds/LMA_Green_Loan_Principles_Booklet-220318.pdf.
- **adaptedFrom**: https://www.prince2.com/usa/blog/project-vs-programme
- **adaptedFrom** (en): https://www.lma.eu.com/application/files/8916/9755/2443/Green_Loan_Principles_23_February_2023.pdf
- **explanatoryNote** (en): Green projects must align with established green finance principles, such as the Green Loan Principles (GLP) issued by the Loan Market Association (LMA), or other recognized sustainability frameworks.
- **explanatoryNote** (en): The borrower must demonstrate that the project meets predefined eligibility criteria for green financing. These criteria are usually aligned with the taxonomy or standards set forth by the Green Loan Principles, the EU Taxonomy for Sustainable Activities, or other regional or international guidelines.
- **explanatoryNote** (en): To qualify as a green project within a green loan: (a) the project must meet use-of-proceeds requirements, meaning that funds must be exclusively allocated to activities that qualify as green, (b) the borrower must establish clear processes for evaluating and selecting eligible projects, (c) there must be transparency in how funds are managed and allocated, often verified through audits or certifications, and (d) the borrower must report regularly on the environmental impact of the project, typically through measurable metrics (e.g., tons of CO₂ avoided, energy saved).

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
