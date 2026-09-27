---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: contractual capability
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: the capacity to enter into legally binding contracts
  - predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: This is the capacity which defines Contractually Capable Entity (sometimes labeled as 'Legal Entity') as distinct
      from 'Legal Person'. In the latter case the liabilities incurred in the contract accrue also to the Legal Person. In
      the case of contractual capability, the entity has the authority to enter into contracts, whether or not the liabilities
      accrue to that same entity (which they do if it is also a Legal Person). For Legal Entities which are not Legal Persons,
      the liability unwinds to some legal person within the structure of the entity, for example a General Partner or a Trustee.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Law/LegalCapacity/LegalCapacity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/LegalCapacity
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/ContractualCapability
sources:
- id: fibo-source-544b6eb4c7
  resource: references/fibo/FND/Law/LegalCapacity.rdf
  sha256: 544b6eb4c7d0acd6efdeb794a9af17ec89bec5145b178192396defaa50bbef22
  title: FIBO source FND/Law/LegalCapacity.rdf
title: contractual capability
type: Ontology Class
---

# contractual capability

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/ContractualCapability>

## Definition

the capacity to enter into legally binding contracts

## Relationships

- **Subclass of**: [LegalCapacity](/concepts/fibo/FND/Law/LegalCapacity/LegalCapacity.md)

## Annotations

- **label** (en): contractual capability
- **definition**: the capacity to enter into legally binding contracts
- **editorialNote**: This is the capacity which defines Contractually Capable Entity (sometimes labeled as 'Legal Entity') as distinct from 'Legal Person'. In the latter case the liabilities incurred in the contract accrue also to the Legal Person. In the case of contractual capability, the entity has the authority to enter into contracts, whether or not the liabilities accrue to that same entity (which they do if it is also a Legal Person). For Legal Entities which are not Legal Persons, the liability unwinds to some legal person within the structure of the entity, for example a General Partner or a Trustee.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
