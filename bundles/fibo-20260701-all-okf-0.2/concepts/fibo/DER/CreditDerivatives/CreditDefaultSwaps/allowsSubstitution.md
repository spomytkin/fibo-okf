---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: allows substitution
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates whether it is possible to substitute other obligations in place of the specified deliverable obligation
  domain:
  - concept: /concepts/fibo/DER/CreditDerivatives/CreditDefaultSwaps/CreditProtectionTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/CreditProtectionTerms
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#boolean
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/allowsSubstitution
sources:
- id: fibo-source-e4f8942a4f
  resource: references/fibo/DER/CreditDerivatives/CreditDefaultSwaps.rdf
  sha256: e4f8942a4f125b0417240813e72a1c570b85cedb764dc5b88ed0663322233d4f
  title: FIBO source DER/CreditDerivatives/CreditDefaultSwaps.rdf
title: allows substitution
type: Ontology Property
---

# allows substitution

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/CreditDerivatives/CreditDefaultSwaps/allowsSubstitution>

## Definition

indicates whether it is possible to substitute other obligations in place of the specified deliverable obligation

## Relationships

- **Domain**: [CreditProtectionTerms](/concepts/fibo/DER/CreditDerivatives/CreditDefaultSwaps/CreditProtectionTerms.md)
- **Range**: [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label** (en): allows substitution
- **definition** (en): indicates whether it is possible to substitute other obligations in place of the specified deliverable obligation

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
