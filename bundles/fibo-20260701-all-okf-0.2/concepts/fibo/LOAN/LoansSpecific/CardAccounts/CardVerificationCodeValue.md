---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: card verification code or value
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: code that specifies either (1) magnetic-stripe data, or (2) printed security features that are used to protect
      data integrity and limit alteration, counterfeiting and fraud generally
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.pcisecuritystandards.org/pci_security/glossary
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/PaymentCard
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  - cardinality: 1
    filler: http://www.w3.org/2001/XMLSchema#string
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Designators/hasTag
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/CodesAndCodeSets/CodeElement
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/CardVerificationCodeValue
sources:
- id: fibo-source-dece66f4c9
  resource: references/fibo/LOAN/LoansSpecific/CardAccounts.rdf
  sha256: dece66f4c9b1f239652e87cc348f748a4ba083249a57e8f2f3c688bfe30e2f19
  title: FIBO source LOAN/LoansSpecific/CardAccounts.rdf
title: card verification code or value
type: Ontology Class
---

# card verification code or value

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/CardVerificationCodeValue>

## Definition

code that specifies either (1) magnetic-stripe data, or (2) printed security features that are used to protect data integrity and limit alteration, counterfeiting and fraud generally

## Relationships

- **Subclass of**: [CodeElement](<https://www.omg.org/spec/Commons/CodesAndCodeSets/CodeElement>)

## Constraints

- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: some values from of type [PaymentCard](/concepts/fibo/LOAN/LoansSpecific/CardAccounts/PaymentCard.md)
- **[hasTag](<https://www.omg.org/spec/Commons/Designators/hasTag>)**: exact qualified cardinality 1 of type [string](<http://www.w3.org/2001/XMLSchema#string>)

## Annotations

- **label**: card verification code or value
- **definition**: code that specifies either (1) magnetic-stripe data, or (2) printed security features that are used to protect data integrity and limit alteration, counterfeiting and fraud generally
- **adaptedFrom**: https://www.pcisecuritystandards.org/pci_security/glossary

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
