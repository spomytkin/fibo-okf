---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/source
    value: https://www.actusfrf.org/taxonomy
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract type - boundary controlled switch
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: cashflow classifier that applies to derivative contracts with subcontract legs which can be activated (knocked
      in) or extinguished (knocked out) when the underlying asset price reaches a specified value
  - predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: Need to figure out what restrictions are needed on derivative instrument to limit the coverage to the right set
      of agreements, and then map to those.
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: The underlying asset may be a stock, index, or exchange-traded fund. Boundary controlled switch contracts with
      a single boundary are currently defined.
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/hasCoverageDescription
    value: Knock-in and Knock-out barrier options with a single boundary. Bonus contracts with payout when underlying asset
      price remains above or below a specified level for specified period.
  - predicate: https://www.omg.org/spec/Commons/TextDatatype/hasTextValue
    value: BCS
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/ACTUSContractType
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSTaxonomy/AlgorithmicContractCategory-Asymmetric.md
    predicate: http://www.w3.org/2004/02/skos/core#isNarrowerThan
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/AlgorithmicContractCategory-Asymmetric
  - concept: /concepts/fibo/ACTUS/ACTUSTaxonomy/AlgorithmicContractFamily-Combined.md
    predicate: http://www.w3.org/2004/02/skos/core#isNarrowerThan
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/AlgorithmicContractFamily-Combined
  - concept: /concepts/fibo/ACTUS/ACTUSTaxonomy/AlgorithmicContractTypesClassificationScheme.md
    predicate: https://www.omg.org/spec/Commons/Collections/isMemberOf
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/AlgorithmicContractTypesClassificationScheme
  - concept: /concepts/fibo/ACTUS/ACTUSTaxonomy/AlgorithmicContractTypesClassificationScheme.md
    predicate: https://www.omg.org/spec/Commons/Designators/isDefinedIn
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/AlgorithmicContractTypesClassificationScheme
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/ACTUSContractType-BoundaryControlledSwitch
sources:
- id: fibo-source-1ffe76217e
  resource: references/fibo/ACTUS/ACTUSContractTermMapping.rdf
  sha256: 1ffe76217e0123653c8a4d03290dcfab352af9fe7a5cdb369ae0e86c55d11bbd
  title: FIBO source ACTUS/ACTUSContractTermMapping.rdf
- id: fibo-source-c715cd4f2e
  resource: references/fibo/ACTUS/ACTUSTaxonomy.rdf
  sha256: c715cd4f2e23f8986a6965786f676ee8eeea6c0496f96a0dd57306fe5907a24a
  title: FIBO source ACTUS/ACTUSTaxonomy.rdf
title: ACTUS contract type - boundary controlled switch
type: Ontology Individual
---

# ACTUS contract type - boundary controlled switch

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/ACTUSContractType-BoundaryControlledSwitch>

## Definition

cashflow classifier that applies to derivative contracts with subcontract legs which can be activated (knocked in) or extinguished (knocked out) when the underlying asset price reaches a specified value

## Relationships

- **Related to**: [AlgorithmicContractCategory-Asymmetric](/concepts/fibo/ACTUS/ACTUSTaxonomy/AlgorithmicContractCategory-Asymmetric.md)
- **Related to**: [AlgorithmicContractFamily-Combined](/concepts/fibo/ACTUS/ACTUSTaxonomy/AlgorithmicContractFamily-Combined.md)
- **Related to**: [AlgorithmicContractTypesClassificationScheme](/concepts/fibo/ACTUS/ACTUSTaxonomy/AlgorithmicContractTypesClassificationScheme.md)
- **Related to**: [AlgorithmicContractTypesClassificationScheme](/concepts/fibo/ACTUS/ACTUSTaxonomy/AlgorithmicContractTypesClassificationScheme.md)

## Annotations

- **source**: https://www.actusfrf.org/taxonomy
- **label**: ACTUS contract type - boundary controlled switch
- **definition**: cashflow classifier that applies to derivative contracts with subcontract legs which can be activated (knocked in) or extinguished (knocked out) when the underlying asset price reaches a specified value
- **editorialNote**: Need to figure out what restrictions are needed on derivative instrument to limit the coverage to the right set of agreements, and then map to those.
- **note**: The underlying asset may be a stock, index, or exchange-traded fund. Boundary controlled switch contracts with a single boundary are currently defined.
- **hasCoverageDescription**: Knock-in and Knock-out barrier options with a single boundary. Bonus contracts with payout when underlying asset price remains above or below a specified level for specified period.
- **hasTextValue**: BCS

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
