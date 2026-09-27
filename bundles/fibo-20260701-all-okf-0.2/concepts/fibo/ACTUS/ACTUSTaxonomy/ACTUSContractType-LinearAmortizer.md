---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/source
    value: https://www.actusfrf.org/taxonomy
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract type - linear amortizer
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: cashflow classifier that applies to contracts whose principal is paid fully at the initial exchange date and where
      the principal is repaid in equal amounts until maturity, with interest payments decreasing accordingly
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: Interest payments decrease over time as the outstanding principal reduces.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/hasCoverageDescription
    value: Standard amortizing loans with fixed principal repayments.
  - predicate: https://www.omg.org/spec/Commons/TextDatatype/hasTextValue
    value: LAM
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/ACTUSContractType
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSTaxonomy/AlgorithmicContractCategory-FixedIncome.md
    predicate: http://www.w3.org/2004/02/skos/core#isNarrowerThan
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/AlgorithmicContractCategory-FixedIncome
  - concept: /concepts/fibo/ACTUS/ACTUSTaxonomy/AlgorithmicContractFamily-Basic.md
    predicate: http://www.w3.org/2004/02/skos/core#isNarrowerThan
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/AlgorithmicContractFamily-Basic
  - concept: /concepts/fibo/ACTUS/ACTUSTaxonomy/AlgorithmicContractTypesClassificationScheme.md
    predicate: https://www.omg.org/spec/Commons/Collections/isMemberOf
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/AlgorithmicContractTypesClassificationScheme
  - concept: /concepts/fibo/ACTUS/ACTUSTaxonomy/AlgorithmicContractTypesClassificationScheme.md
    predicate: https://www.omg.org/spec/Commons/Designators/isDefinedIn
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/AlgorithmicContractTypesClassificationScheme
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/ACTUSContractType-LinearAmortizer
sources:
- id: fibo-source-1ffe76217e
  resource: references/fibo/ACTUS/ACTUSContractTermMapping.rdf
  sha256: 1ffe76217e0123653c8a4d03290dcfab352af9fe7a5cdb369ae0e86c55d11bbd
  title: FIBO source ACTUS/ACTUSContractTermMapping.rdf
- id: fibo-source-c715cd4f2e
  resource: references/fibo/ACTUS/ACTUSTaxonomy.rdf
  sha256: c715cd4f2e23f8986a6965786f676ee8eeea6c0496f96a0dd57306fe5907a24a
  title: FIBO source ACTUS/ACTUSTaxonomy.rdf
title: ACTUS contract type - linear amortizer
type: Ontology Individual
---

# ACTUS contract type - linear amortizer

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/ACTUSContractType-LinearAmortizer>

## Definition

cashflow classifier that applies to contracts whose principal is paid fully at the initial exchange date and where the principal is repaid in equal amounts until maturity, with interest payments decreasing accordingly

## Relationships

- **Related to**: [AlgorithmicContractCategory-FixedIncome](/concepts/fibo/ACTUS/ACTUSTaxonomy/AlgorithmicContractCategory-FixedIncome.md)
- **Related to**: [AlgorithmicContractFamily-Basic](/concepts/fibo/ACTUS/ACTUSTaxonomy/AlgorithmicContractFamily-Basic.md)
- **Related to**: [AlgorithmicContractTypesClassificationScheme](/concepts/fibo/ACTUS/ACTUSTaxonomy/AlgorithmicContractTypesClassificationScheme.md)
- **Related to**: [AlgorithmicContractTypesClassificationScheme](/concepts/fibo/ACTUS/ACTUSTaxonomy/AlgorithmicContractTypesClassificationScheme.md)

## Annotations

- **source**: https://www.actusfrf.org/taxonomy
- **label**: ACTUS contract type - linear amortizer
- **definition**: cashflow classifier that applies to contracts whose principal is paid fully at the initial exchange date and where the principal is repaid in equal amounts until maturity, with interest payments decreasing accordingly
- **note**: Interest payments decrease over time as the outstanding principal reduces.
- **hasCoverageDescription**: Standard amortizing loans with fixed principal repayments.
- **hasTextValue**: LAM

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
