---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/source
    value: https://www.actusfrf.org/taxonomy
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: algorithmic contract family - combined
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: contract family classifier that applies to combined (complex, derived) contracts, such as derivatives
  - predicate: https://www.omg.org/spec/Commons/TextDatatype/hasTextValue
    value: Combined
  different_from:
  - concept: /concepts/fibo/ACTUS/ACTUSTaxonomy/AlgorithmicContractFamily-Basic.md
    predicate: http://www.w3.org/2002/07/owl#differentFrom
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/AlgorithmicContractFamily-Basic
  - concept: /concepts/fibo/ACTUS/ACTUSTaxonomy/AlgorithmicContractFamily-CreditEnhancement.md
    predicate: http://www.w3.org/2002/07/owl#differentFrom
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/AlgorithmicContractFamily-CreditEnhancement
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/AlgorithmicContractFamily
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSTaxonomy/AlgorithmicContractTypesClassificationScheme.md
    predicate: https://www.omg.org/spec/Commons/Collections/isMemberOf
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/AlgorithmicContractTypesClassificationScheme
  - concept: /concepts/fibo/ACTUS/ACTUSTaxonomy/AlgorithmicContractTypesClassificationScheme.md
    predicate: https://www.omg.org/spec/Commons/Designators/isDefinedIn
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/AlgorithmicContractTypesClassificationScheme
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/AlgorithmicContractFamily-Combined
sources:
- id: fibo-source-c715cd4f2e
  resource: references/fibo/ACTUS/ACTUSTaxonomy.rdf
  sha256: c715cd4f2e23f8986a6965786f676ee8eeea6c0496f96a0dd57306fe5907a24a
  title: FIBO source ACTUS/ACTUSTaxonomy.rdf
title: algorithmic contract family - combined
type: Ontology Individual
---

# algorithmic contract family - combined

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/AlgorithmicContractFamily-Combined>

## Definition

contract family classifier that applies to combined (complex, derived) contracts, such as derivatives

## Relationships

- **Different from**: [AlgorithmicContractFamily-Basic](/concepts/fibo/ACTUS/ACTUSTaxonomy/AlgorithmicContractFamily-Basic.md)
- **Different from**: [AlgorithmicContractFamily-CreditEnhancement](/concepts/fibo/ACTUS/ACTUSTaxonomy/AlgorithmicContractFamily-CreditEnhancement.md)
- **Related to**: [AlgorithmicContractTypesClassificationScheme](/concepts/fibo/ACTUS/ACTUSTaxonomy/AlgorithmicContractTypesClassificationScheme.md)
- **Related to**: [AlgorithmicContractTypesClassificationScheme](/concepts/fibo/ACTUS/ACTUSTaxonomy/AlgorithmicContractTypesClassificationScheme.md)

## Annotations

- **source**: https://www.actusfrf.org/taxonomy
- **label**: algorithmic contract family - combined
- **definition**: contract family classifier that applies to combined (complex, derived) contracts, such as derivatives
- **hasTextValue**: Combined

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
