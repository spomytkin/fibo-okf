---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: power of attorney
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: legal authorization given by one party (the principal) to another (the agent or attorney-in-fact) to perform certain
      acts on the principal's behalf
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The appointment can be effective immediately or if the principal is unable to make decisions or perform certain
      actions on their own. It may be a (1) general power of attorney that authorizes the agent to act generally on behalf
      of the principal, such as to transfer funds from one account to another, pay debts, make investments, and so forth,
      or (2) limited to a specific act or situation, such as for management of an individual's finances in a single account,
      such as a brokerage account, or for management of healthcare. Decisions made and actions taken by an attorney in fact
      (within the scope of his or her authority) are legally binding on the principal.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/Date
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/hasEffectiveDate
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/LegallyCompetentNaturalPerson
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/isConferredOn
  subclass_of:
  - concept: /concepts/fibo/FND/Law/LegalCapacity/LegalCapacity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/LegalCapacity
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/PowerOfAttorney
sources:
- id: fibo-source-5d6bb270b5
  resource: references/fibo/BE/LegalEntities/LegalPersons.rdf
  sha256: 5d6bb270b50e9a3b5bf8d32aa2448ba56a3e1b9880a137cb89b1bdb2d7811196
  title: FIBO source BE/LegalEntities/LegalPersons.rdf
title: power of attorney
type: Ontology Class
---

# power of attorney

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/PowerOfAttorney>

## Definition

legal authorization given by one party (the principal) to another (the agent or attorney-in-fact) to perform certain acts on the principal's behalf

## Relationships

- **Subclass of**: [LegalCapacity](/concepts/fibo/FND/Law/LegalCapacity/LegalCapacity.md)

## Constraints

- **[hasEffectiveDate](/concepts/fibo/FND/Agreements/Contracts/hasEffectiveDate.md)**: min qualified cardinality 0 of type [Date](<https://www.omg.org/spec/Commons/DatesAndTimes/Date>)
- **[isConferredOn](/concepts/fibo/FND/Law/LegalCapacity/isConferredOn.md)**: some values from of type [LegallyCompetentNaturalPerson](/concepts/fibo/BE/LegalEntities/LegalPersons/LegallyCompetentNaturalPerson.md)

## Annotations

- **label**: power of attorney
- **definition**: legal authorization given by one party (the principal) to another (the agent or attorney-in-fact) to perform certain acts on the principal's behalf
- **explanatoryNote**: The appointment can be effective immediately or if the principal is unable to make decisions or perform certain actions on their own. It may be a (1) general power of attorney that authorizes the agent to act generally on behalf of the principal, such as to transfer funds from one account to another, pay debts, make investments, and so forth, or (2) limited to a specific act or situation, such as for management of an individual's finances in a single account, such as a brokerage account, or for management of healthcare. Decisions made and actions taken by an attorney in fact (within the scope of his or her authority) are legally binding on the principal.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
