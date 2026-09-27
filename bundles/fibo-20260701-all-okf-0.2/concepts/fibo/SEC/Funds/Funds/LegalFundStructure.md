---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: legal fund structure
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: structure of a fund with respect to its legal formation in some jurisdiction
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RegulatoryAgencies/isGovernedBy
  subclass_of:
  - concept: /concepts/fibo/FND/Law/LegalCapacity/LegalConstruct.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/LegalConstruct
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/LegalFundStructure
sources:
- id: fibo-source-a82c11f42e
  resource: references/fibo/SEC/Funds/Funds.rdf
  sha256: a82c11f42ef79a0f83aeae8434ad054ddef746da9d97126ef3d8923eacf9c275
  title: FIBO source SEC/Funds/Funds.rdf
title: legal fund structure
type: Ontology Class
---

# legal fund structure

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/LegalFundStructure>

## Definition

structure of a fund with respect to its legal formation in some jurisdiction

## Relationships

- **Subclass of**: [LegalConstruct](/concepts/fibo/FND/Law/LegalCapacity/LegalConstruct.md)

## Constraints

- **[isGovernedBy](<https://www.omg.org/spec/Commons/RegulatoryAgencies/isGovernedBy>)**: some values from of type [Jurisdiction](<https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction>)

## Annotations

- **label** (en): legal fund structure
- **definition** (en): structure of a fund with respect to its legal formation in some jurisdiction

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
