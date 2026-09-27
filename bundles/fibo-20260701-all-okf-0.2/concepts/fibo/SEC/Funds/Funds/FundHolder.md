---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: fund holder
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party that owns units in or a percentage of and has rights and responsibilities with respect to some fund, provided
      in exchange for investment
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Note that in some cases the concept of 'fund holder' may be synonymous with shareholder, but not all.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/BE/OwnershipAndControl/CorporateOwnership/BeneficialOwner.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateOwnership/BeneficialOwner
  - concept: /concepts/fibo/FND/Agreements/Contracts/Counterparty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/Counterparty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/FundHolder
sources:
- id: fibo-source-a82c11f42e
  resource: references/fibo/SEC/Funds/Funds.rdf
  sha256: a82c11f42ef79a0f83aeae8434ad054ddef746da9d97126ef3d8923eacf9c275
  title: FIBO source SEC/Funds/Funds.rdf
title: fund holder
type: Ontology Class
---

# fund holder

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/FundHolder>

## Definition

party that owns units in or a percentage of and has rights and responsibilities with respect to some fund, provided in exchange for investment

## Relationships

- **Subclass of**: [BeneficialOwner](/concepts/fibo/BE/OwnershipAndControl/CorporateOwnership/BeneficialOwner.md)
- **Subclass of**: [Counterparty](/concepts/fibo/FND/Agreements/Contracts/Counterparty.md)

## Annotations

- **label**: fund holder
- **definition**: party that owns units in or a percentage of and has rights and responsibilities with respect to some fund, provided in exchange for investment
- **explanatoryNote**: Note that in some cases the concept of 'fund holder' may be synonymous with shareholder, but not all.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
