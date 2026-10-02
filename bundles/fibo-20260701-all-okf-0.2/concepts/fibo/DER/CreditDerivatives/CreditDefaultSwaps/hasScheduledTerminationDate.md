---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has scheduled termination date
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: date on which credit protection is due to expire as agreed by both parties
  domain:
  - concept: /concepts/fibo/DER/CreditDerivatives/CreditDefaultSwaps/CreditProtectionTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/CreditProtectionTerms
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Arrangements/Documents/hasTerminationDate.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Documents/hasTerminationDate
resource: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/hasScheduledTerminationDate
sources:
- id: fibo-source-e4f8942a4f
  resource: references/fibo/DER/CreditDerivatives/CreditDefaultSwaps.rdf
  sha256: e4f8942a4f125b0417240813e72a1c570b85cedb764dc5b88ed0663322233d4f
  title: FIBO source DER/CreditDerivatives/CreditDefaultSwaps.rdf
title: has scheduled termination date
type: Ontology Property
---

# has scheduled termination date

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/hasScheduledTerminationDate>

## Definition

date on which credit protection is due to expire as agreed by both parties

## Relationships

- **Domain**: [CreditProtectionTerms](/concepts/fibo/DER/CreditDerivatives/CreditDefaultSwaps/CreditProtectionTerms.md)
- **Range**: [ExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate>)
- **Subproperty of**: [hasTerminationDate](/concepts/fibo/FND/Arrangements/Documents/hasTerminationDate.md)

## Annotations

- **label** (en): has scheduled termination date
- **definition** (en): date on which credit protection is due to expire as agreed by both parties

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
