---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: primary card account number
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: composite identifier of 14 or 16 digits embossed on a bank or payment card and encoded in the card's magnetic strip
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: PAN
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The PAN identifies the issuer of the card and the account including part of the account number, and contains a
      check digit that verifies the authenticity of the embossed account number.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: primary account number
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/CardAccount
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Identifiers/identifies
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/AccountIdentifier.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/ClientsAndAccounts/AccountIdentifier
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/PrimaryCardAccountNumber
sources:
- id: fibo-source-dece66f4c9
  resource: references/fibo/LOAN/LoansSpecific/CardAccounts.rdf
  sha256: dece66f4c9b1f239652e87cc348f748a4ba083249a57e8f2f3c688bfe30e2f19
  title: FIBO source LOAN/LoansSpecific/CardAccounts.rdf
title: primary card account number
type: Ontology Class
---

# primary card account number

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/CardAccounts/PrimaryCardAccountNumber>

## Definition

composite identifier of 14 or 16 digits embossed on a bank or payment card and encoded in the card's magnetic strip

## Relationships

- **Subclass of**: [AccountIdentifier](/concepts/fibo/FBC/ProductsAndServices/ClientsAndAccounts/AccountIdentifier.md)

## Constraints

- **[identifies](<https://www.omg.org/spec/Commons/Identifiers/identifies>)**: exact qualified cardinality 1 of type [CardAccount](/concepts/fibo/LOAN/LoansSpecific/CardAccounts/CardAccount.md)

## Annotations

- **label**: primary card account number
- **definition**: composite identifier of 14 or 16 digits embossed on a bank or payment card and encoded in the card's magnetic strip
- **abbreviation**: PAN
- **explanatoryNote**: The PAN identifies the issuer of the card and the account including part of the account number, and contains a check digit that verifies the authenticity of the embossed account number.
- **synonym**: primary account number

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
