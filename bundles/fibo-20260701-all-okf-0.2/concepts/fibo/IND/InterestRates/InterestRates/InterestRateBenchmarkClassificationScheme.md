---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: interest rate benchmark classification scheme
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: scheme for classifying interest rate benchmarks, such as the FpML classification scheme
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/InterestRateBenchmark
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/defines
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Classifiers/ClassificationScheme
resource: https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/InterestRateBenchmarkClassificationScheme
sources:
- id: fibo-source-e2bedd1809
  resource: references/fibo/IND/InterestRates/InterestRates.rdf
  sha256: e2bedd18096c7346ecdd7687f4fbb370e828c7fc4e483bd84780e67e65d77fe1
  title: FIBO source IND/InterestRates/InterestRates.rdf
title: interest rate benchmark classification scheme
type: Ontology Class
---

# interest rate benchmark classification scheme

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/InterestRates/InterestRates/InterestRateBenchmarkClassificationScheme>

## Definition

scheme for classifying interest rate benchmarks, such as the FpML classification scheme

## Relationships

- **Subclass of**: [ClassificationScheme](<https://www.omg.org/spec/Commons/Classifiers/ClassificationScheme>)

## Constraints

- **[defines](<https://www.omg.org/spec/Commons/Designators/defines>)**: some values from of type [InterestRateBenchmark](/concepts/fibo/IND/InterestRates/InterestRates/InterestRateBenchmark.md)

## Annotations

- **label**: interest rate benchmark classification scheme
- **definition**: scheme for classifying interest rate benchmarks, such as the FpML classification scheme

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
