---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: death certificate
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: original document certifying the circumstances of the death (such as how and when it occurred), or a certified
      copy of or representation of the ensuing registration of that death
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A death certificate is a vital record documenting information (including age, occupation, place of birth, place
      of residence, and often identifying the parents and possibly spouse of the deceased) relating to a dead person and including
      a doctor's certification of the cause of death.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/DateOfDeath
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/isEvidenceFor
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/DeathCertificateIdentifier
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy
  subclass_of:
  - concept: /concepts/fibo/FND/AgentsAndPeople/People/IdentityDocument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/IdentityDocument
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Documents/Certificate
resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/DeathCertificate
sources:
- id: fibo-source-ad5313f34d
  resource: references/fibo/FND/AgentsAndPeople/People.rdf
  sha256: ad5313f34d5a14c86455f952c2daeb486e6560ce3168a66d7e1c262b492c22ae
  title: FIBO source FND/AgentsAndPeople/People.rdf
- id: fibo-source-310cd83e5e
  resource: references/fibo/FND/Agreements/Contracts.rdf
  sha256: 310cd83e5e80f369e3f18c0a064ecf0f9519dae374fd89af25778d1089321ed8
  title: FIBO source FND/Agreements/Contracts.rdf
title: death certificate
type: Ontology Class
---

# death certificate

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/DeathCertificate>

## Definition

original document certifying the circumstances of the death (such as how and when it occurred), or a certified copy of or representation of the ensuing registration of that death

## Relationships

- **Subclass of**: [IdentityDocument](/concepts/fibo/FND/AgentsAndPeople/People/IdentityDocument.md)
- **Subclass of**: [Certificate](<https://www.omg.org/spec/Commons/Documents/Certificate>)

## Constraints

- **[isEvidenceFor](/concepts/fibo/FND/Agreements/Contracts/isEvidenceFor.md)**: exact qualified cardinality 1 of type [DateOfDeath](/concepts/fibo/FND/AgentsAndPeople/People/DateOfDeath.md)
- **[isIdentifiedBy](<https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy>)**: exact qualified cardinality 1 of type [DeathCertificateIdentifier](/concepts/fibo/FND/AgentsAndPeople/People/DeathCertificateIdentifier.md)

## Annotations

- **label**: death certificate
- **definition**: original document certifying the circumstances of the death (such as how and when it occurred), or a certified copy of or representation of the ensuing registration of that death
- **explanatoryNote**: A death certificate is a vital record documenting information (including age, occupation, place of birth, place of residence, and often identifying the parents and possibly spouse of the deceased) relating to a dead person and including a doctor's certification of the cause of death.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
