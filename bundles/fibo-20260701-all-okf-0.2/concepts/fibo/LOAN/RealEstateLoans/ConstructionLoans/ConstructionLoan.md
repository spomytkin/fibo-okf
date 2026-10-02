---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: construction loan
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: loan covering construction and development costs, secured by a mortgage on the property financed
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A construction loan credit facility tranche (sub-facility) is a portion of a construction loan that is released
      in stages, or tranches, to fund specific phases of a construction project. Each tranche (committed sub-facility) is
      released once the borrower reaches a certain milestone, such as pouring concrete or completing the foundation. The borrower
      typically only pays interest on the amount that has been released at any given time.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The Project Management Institute (PMI) breaks down most construction projects into five phases, which are initiation,
      planning, execution, monitoring and control, and closeout. Construction loans also typically include milestones at which
      a portion of the total facility is advanced to the borrower given proof of completion or meeting other requirements
      with respect to the work.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Places/RealProperty/RealProperty
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/isCollateralizedBy
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractMilestone
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasMilestoneProvision
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/CreditFacility.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/CreditFacility
  - concept: /concepts/fibo/FND/Agreements/Contracts/MasterAgreement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/MasterAgreement
  - concept: /concepts/fibo/LOAN/LoansGeneral/Loans/CollateralizedLoan.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/CollateralizedLoan
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/ConstructionLoans/ConstructionLoan
sources:
- id: fibo-source-c8807a0349
  resource: references/fibo/LOAN/RealEstateLoans/ConstructionLoans.rdf
  sha256: c8807a0349286758472a44895c182ef590265f17f0b2af37b0bdae6d5c206f68
  title: FIBO source LOAN/RealEstateLoans/ConstructionLoans.rdf
title: construction loan
type: Ontology Class
---

# construction loan

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/ConstructionLoans/ConstructionLoan>

## Definition

loan covering construction and development costs, secured by a mortgage on the property financed

## Relationships

- **Subclass of**: [CreditFacility](/concepts/fibo/FBC/DebtAndEquities/Debt/CreditFacility.md)
- **Subclass of**: [MasterAgreement](/concepts/fibo/FND/Agreements/Contracts/MasterAgreement.md)
- **Subclass of**: [CollateralizedLoan](/concepts/fibo/LOAN/LoansGeneral/Loans/CollateralizedLoan.md)

## Constraints

- **[isCollateralizedBy](/concepts/fibo/FBC/DebtAndEquities/Debt/isCollateralizedBy.md)**: min qualified cardinality 0 of type [RealProperty](/concepts/fibo/FND/Places/RealProperty/RealProperty.md)
- **[hasMilestoneProvision](/concepts/fibo/FND/Agreements/Contracts/hasMilestoneProvision.md)**: min qualified cardinality 0 of type [ContractMilestone](/concepts/fibo/FND/Agreements/Contracts/ContractMilestone.md)

## Annotations

- **label** (en): construction loan
- **definition** (en): loan covering construction and development costs, secured by a mortgage on the property financed
- **explanatoryNote** (en): A construction loan credit facility tranche (sub-facility) is a portion of a construction loan that is released in stages, or tranches, to fund specific phases of a construction project. Each tranche (committed sub-facility) is released once the borrower reaches a certain milestone, such as pouring concrete or completing the foundation. The borrower typically only pays interest on the amount that has been released at any given time.
- **explanatoryNote** (en): The Project Management Institute (PMI) breaks down most construction projects into five phases, which are initiation, planning, execution, monitoring and control, and closeout. Construction loans also typically include milestones at which a portion of the total facility is advanced to the borrower given proof of completion or meeting other requirements with respect to the work.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
