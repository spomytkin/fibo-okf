---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: loan prepayment formula
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The formula which embodies the model for loan pool prepayment speed.
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: 'From SMER sessions: This is a model. Includes other factors such as homogeniety. To model this more completely
      we need to identify the parameters that go in to this formula. Among these is the above homogeneity measure - need to
      know how that is measured and in what terms it is expressed, e.g. as a percentage, with reference to some mean or standard
      deviation and so on. Also some of the parameters used in this model would presumably make reference to standard mathematical
      model constructs such as normal distribution, variaous deviation measures, Chi squared and so on. These are not presently
      in the semantics model, but can be modeled semantically if required. This would not however be a mathematical model
      - we only need to identify these and show meaningful relationships (not mathematical relationships) between them.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Utilities/Analytics/Formula.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/Analytics/Formula
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/LoanPrepaymentFormula
sources:
- id: fibo-source-4a5facbded
  resource: references/fibo/MD/DebtTemporal/DebtAnalytics.rdf
  sha256: 4a5facbdedf24373f412662d54858a7e9bb5e857cf4bc60543d124abfb92804a
  title: FIBO source MD/DebtTemporal/DebtAnalytics.rdf
title: loan prepayment formula
type: Ontology Class
---

# loan prepayment formula

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/LoanPrepaymentFormula>

## Definition

The formula which embodies the model for loan pool prepayment speed.

## Relationships

- **Subclass of**: [Formula](/concepts/fibo/FND/Utilities/Analytics/Formula.md)

## Annotations

- **label** (en): loan prepayment formula
- **definition** (en): The formula which embodies the model for loan pool prepayment speed.
- **editorialNote** (en): From SMER sessions: This is a model. Includes other factors such as homogeniety. To model this more completely we need to identify the parameters that go in to this formula. Among these is the above homogeneity measure - need to know how that is measured and in what terms it is expressed, e.g. as a percentage, with reference to some mean or standard deviation and so on. Also some of the parameters used in this model would presumably make reference to standard mathematical model constructs such as normal distribution, variaous deviation measures, Chi squared and so on. These are not presently in the semantics model, but can be modeled semantically if required. This would not however be a mathematical model - we only need to identify these and show meaningful relationships (not mathematical relationships) between them.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
