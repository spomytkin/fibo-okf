---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: public record category
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: classifier of public records relevant to a loan application, e.g. tax lien, wage garnishment, foreclosure
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Classifiers/Classifier
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/PublicRecordCategory
sources:
- id: fibo-source-8202fa75b9
  resource: references/fibo/LOAN/LoansGeneral/LoanApplications.rdf
  sha256: 8202fa75b97c33c23b62b818e5df80b122af94dadc7ccf42fe9266d72d61445e
  title: FIBO source LOAN/LoansGeneral/LoanApplications.rdf
title: public record category
type: Ontology Class
---

# public record category

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanApplications/PublicRecordCategory>

## Definition

classifier of public records relevant to a loan application, e.g. tax lien, wage garnishment, foreclosure

## Relationships

- **Subclass of**: [Classifier](<https://www.omg.org/spec/Commons/Classifiers/Classifier>)

## Annotations

- **label**: public record category
- **definition**: classifier of public records relevant to a loan application, e.g. tax lien, wage garnishment, foreclosure

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
