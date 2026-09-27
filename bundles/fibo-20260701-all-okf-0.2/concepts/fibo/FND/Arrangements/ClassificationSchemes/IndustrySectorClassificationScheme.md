---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: industry sector classification scheme
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: system for allocating classifiers to organizations by industry sector
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: Examples include the North American Industry Classification System (NAICS) and Standardized Industry Classification
      (SIC) in the U.S. and Canada, and the NACE (Nomenclature Générale des Activités Économiques dans les Communautés Européennes)
      in the EU, developed by governments to classify industries. They also include commercial classification schemes, such
      as the Global Industry Standard Classification (GICS) developed jointly by Morgan Stanley Capital International (MSCI)
      and Standard and Poor's, and competing schemes including the Industry Classification Benchmark (ICB) system, maintained
      by Dow Jones and London's FTSE Group, among others.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/ClassificationSchemes/IndustrySectorClassifier
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/defines
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Classifiers/ClassificationScheme
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/ClassificationSchemes/IndustrySectorClassificationScheme
sources:
- id: fibo-source-7338de6177
  resource: references/fibo/FND/Arrangements/ClassificationSchemes.rdf
  sha256: 7338de61776faa661146c3b44c6902fc98da670de604e69439fae05577135627
  title: FIBO source FND/Arrangements/ClassificationSchemes.rdf
title: industry sector classification scheme
type: Ontology Class
---

# industry sector classification scheme

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/ClassificationSchemes/IndustrySectorClassificationScheme>

## Definition

system for allocating classifiers to organizations by industry sector

## Relationships

- **Subclass of**: [ClassificationScheme](<https://www.omg.org/spec/Commons/Classifiers/ClassificationScheme>)

## Constraints

- **[defines](<https://www.omg.org/spec/Commons/Designators/defines>)**: some values from of type [IndustrySectorClassifier](/concepts/fibo/FND/Arrangements/ClassificationSchemes/IndustrySectorClassifier.md)

## Annotations

- **label**: industry sector classification scheme
- **definition**: system for allocating classifiers to organizations by industry sector
- **example**: Examples include the North American Industry Classification System (NAICS) and Standardized Industry Classification (SIC) in the U.S. and Canada, and the NACE (Nomenclature Générale des Activités Économiques dans les Communautés Européennes) in the EU, developed by governments to classify industries. They also include commercial classification schemes, such as the Global Industry Standard Classification (GICS) developed jointly by Morgan Stanley Capital International (MSCI) and Standard and Poor's, and competing schemes including the Industry Classification Benchmark (ICB) system, maintained by Dow Jones and London's FTSE Group, among others.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
