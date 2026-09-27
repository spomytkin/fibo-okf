---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: loan pool prepayment model
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Model of the prepayments of loans in a pool of individual loans, such as a mortgage pool or loan pool.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This model captures the parameters that may influence the prepayment of loans or mortgages and relates these mathematically.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/LoanPrepaymentFormula
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
  subclass_of:
  - concept: /concepts/fibo/FND/Utilities/Analytics/Formula.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/Formula
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/LoanPoolPrepaymentModel
sources:
- id: fibo-source-4a5facbded
  resource: references/fibo/MD/DebtTemporal/DebtAnalytics.rdf
  sha256: 4a5facbdedf24373f412662d54858a7e9bb5e857cf4bc60543d124abfb92804a
  title: FIBO source MD/DebtTemporal/DebtAnalytics.rdf
title: loan pool prepayment model
type: Ontology Class
---

# loan pool prepayment model

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/LoanPoolPrepaymentModel>

## Definition

Model of the prepayments of loans in a pool of individual loans, such as a mortgage pool or loan pool.

## Relationships

- **Subclass of**: [Formula](/concepts/fibo/FND/Utilities/Analytics/Formula.md)

## Constraints

- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from of type [LoanPrepaymentFormula](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/LoanPrepaymentFormula.md)

## Annotations

- **label** (en): loan pool prepayment model
- **definition** (en): Model of the prepayments of loans in a pool of individual loans, such as a mortgage pool or loan pool.
- **explanatoryNote** (en): This model captures the parameters that may influence the prepayment of loans or mortgages and relates these mathematically.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
