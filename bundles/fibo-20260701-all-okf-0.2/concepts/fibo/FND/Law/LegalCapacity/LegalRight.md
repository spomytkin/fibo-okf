---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: legal right
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: personal right, privilege, or benefit that a government, contract, or law provides or protects, making an individual
      or entity eligible to receive something
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A legal right, if challenged, may be supported in court as recognizable and enforceable in law, statutes, regulations,
      or other legislative actions.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This entitlement creates a corresponding obligation for the provider to deliver that benefit.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/LegalObligation
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/implies
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCore/StatuteLaw
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isConferredBy
  - filler: https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/isApplicableIn
  subclass_of:
  - concept: /concepts/fibo/FND/Law/LegalCapacity/Right.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/Right
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/LegalRight
sources:
- id: fibo-source-544b6eb4c7
  resource: references/fibo/FND/Law/LegalCapacity.rdf
  sha256: 544b6eb4c7d0acd6efdeb794a9af17ec89bec5145b178192396defaa50bbef22
  title: FIBO source FND/Law/LegalCapacity.rdf
title: legal right
type: Ontology Class
---

# legal right

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/LegalRight>

## Definition

personal right, privilege, or benefit that a government, contract, or law provides or protects, making an individual or entity eligible to receive something

## Relationships

- **Subclass of**: [Right](/concepts/fibo/FND/Law/LegalCapacity/Right.md)

## Constraints

- **[implies](/concepts/fibo/FND/Law/LegalCapacity/implies.md)**: some values from of type [LegalObligation](/concepts/fibo/FND/Law/LegalCapacity/LegalObligation.md)
- **[isConferredBy](/concepts/fibo/FND/Relations/Relations/isConferredBy.md)**: some values from of type [StatuteLaw](/concepts/fibo/FND/Law/LegalCore/StatuteLaw.md)
- **[isApplicableIn](<https://www.omg.org/spec/Commons/ContextualDesignators/isApplicableIn>)**: some values from of type [Jurisdiction](<https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction>)

## Annotations

- **label**: legal right
- **definition**: personal right, privilege, or benefit that a government, contract, or law provides or protects, making an individual or entity eligible to receive something
- **explanatoryNote**: A legal right, if challenged, may be supported in court as recognizable and enforceable in law, statutes, regulations, or other legislative actions.
- **explanatoryNote**: This entitlement creates a corresponding obligation for the provider to deliver that benefit.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
