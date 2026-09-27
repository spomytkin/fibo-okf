---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: precious metal identifier
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: sequence of characters uniquely identifying the precious metal in some context
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: http://www.w3.org/2001/XMLSchema#string
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Designators/hasTag
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/PreciousMetal
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Identifiers/identifies
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/CodesAndCodeSets/CodeElement
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Identifiers/Identifier
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/PreciousMetalIdentifier
sources:
- id: fibo-source-4355744519
  resource: references/fibo/FND/Accounting/CurrencyAmount.rdf
  sha256: 4355744519e448cbeeedd0e9601a43470dc1329a7cab73d807e7b99048db0032
  title: FIBO source FND/Accounting/CurrencyAmount.rdf
title: precious metal identifier
type: Ontology Class
---

# precious metal identifier

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/PreciousMetalIdentifier>

## Definition

sequence of characters uniquely identifying the precious metal in some context

## Relationships

- **Subclass of**: [CodeElement](<https://www.omg.org/spec/Commons/CodesAndCodeSets/CodeElement>)
- **Subclass of**: [Identifier](<https://www.omg.org/spec/Commons/Identifiers/Identifier>)

## Constraints

- **[hasTag](<https://www.omg.org/spec/Commons/Designators/hasTag>)**: exact qualified cardinality 1 of type [string](<http://www.w3.org/2001/XMLSchema#string>)
- **[identifies](<https://www.omg.org/spec/Commons/Identifiers/identifies>)**: some values from of type [PreciousMetal](/concepts/fibo/FND/Accounting/CurrencyAmount/PreciousMetal.md)

## Annotations

- **label**: precious metal identifier
- **definition**: sequence of characters uniquely identifying the precious metal in some context

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
