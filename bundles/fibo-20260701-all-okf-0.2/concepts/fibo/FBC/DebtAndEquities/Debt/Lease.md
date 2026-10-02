---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: lease
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: credit agreement permitting the use of real estate, equipment or another asset, such as a vehicle, by the owner
      of that asset (the lessor) to a user (the lessee) for a specific period of time in return for payment as specified in
      the agreement
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The lessor is the legal owner of the asset, while the lessee obtains the right to use the asset in return for rental
      payments. The lessee also agrees to abide by various conditions regarding their use of the property or equipment. For
      example, a person leasing a car may agree to the condition that the car will only be used for personal use.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: lease agreement
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: lease contract
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/CreditAgreementRepaidPeriodically.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/CreditAgreementRepaidPeriodically
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Lease
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
title: lease
type: Ontology Class
---

# lease

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Lease>

## Definition

credit agreement permitting the use of real estate, equipment or another asset, such as a vehicle, by the owner of that asset (the lessor) to a user (the lessee) for a specific period of time in return for payment as specified in the agreement

## Relationships

- **Subclass of**: [CreditAgreementRepaidPeriodically](/concepts/fibo/FBC/DebtAndEquities/Debt/CreditAgreementRepaidPeriodically.md)

## Annotations

- **label**: lease
- **definition**: credit agreement permitting the use of real estate, equipment or another asset, such as a vehicle, by the owner of that asset (the lessor) to a user (the lessee) for a specific period of time in return for payment as specified in the agreement
- **explanatoryNote**: The lessor is the legal owner of the asset, while the lessee obtains the right to use the asset in return for rental payments. The lessee also agrees to abide by various conditions regarding their use of the property or equipment. For example, a person leasing a car may agree to the condition that the car will only be used for personal use.
- **synonym**: lease agreement
- **synonym**: lease contract

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
