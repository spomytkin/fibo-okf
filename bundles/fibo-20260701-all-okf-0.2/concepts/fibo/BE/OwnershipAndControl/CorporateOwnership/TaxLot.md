---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: tax lot
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: financial asset that is a block of securities or other financial assets with a distinct cost basis for tax reporting
      purposes
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'Tax lots reflect how shares or other assets are tracked for capital gains and may be adjusted by events including:

      - reinvested dividends (creates very small, new tax lots);

      - stock splits or mergers (adjusts basis, may create fractional lots);

      - Wash sale rules (can change which lots are recognized).

      When an investor sells, they select which tax lot to sell (specific ID, FIFO, etc.), which determines realized gain
      or loss.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: http://www.w3.org/2001/XMLSchema#decimal
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateOwnership/consistsOfNumberOfUnits
  subclass_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership/FinancialAsset.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/FinancialAsset
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateOwnership/TaxLot
sources:
- id: fibo-source-4d1bc90c45
  resource: references/fibo/BE/OwnershipAndControl/CorporateOwnership.rdf
  sha256: 4d1bc90c4583cdc3c4f8228a8afb505706731dd0d76b848f6678e714ee5ac147
  title: FIBO source BE/OwnershipAndControl/CorporateOwnership.rdf
title: tax lot
type: Ontology Class
---

# tax lot

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateOwnership/TaxLot>

## Definition

financial asset that is a block of securities or other financial assets with a distinct cost basis for tax reporting purposes

## Relationships

- **Subclass of**: [FinancialAsset](/concepts/fibo/FND/OwnershipAndControl/Ownership/FinancialAsset.md)

## Constraints

- **[consistsOfNumberOfUnits](/concepts/fibo/BE/OwnershipAndControl/CorporateOwnership/consistsOfNumberOfUnits.md)**: exact qualified cardinality 1 of type [decimal](<http://www.w3.org/2001/XMLSchema#decimal>)

## Annotations

- **label**: tax lot
- **definition**: financial asset that is a block of securities or other financial assets with a distinct cost basis for tax reporting purposes
- **explanatoryNote**: Tax lots reflect how shares or other assets are tracked for capital gains and may be adjusted by events including: - reinvested dividends (creates very small, new tax lots); - stock splits or mergers (adjusts basis, may create fractional lots); - Wash sale rules (can change which lots are recognized). When an investor sells, they select which tax lot to sell (specific ID, FIFO, etc.), which determines realized gain or loss.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
