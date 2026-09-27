---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: certificate of participation
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: debt instrument evidencing a pro rata share in a specific pledged revenue stream, usually lease payments by the
      issuer that are typically subject to annual appropriation
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: COP
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A certificate of participation (COP) is a type of financing where an investor purchases a share of the lease revenues
      of a program rather than the bond being secured by those revenues. The certificate generally entitles the holder to
      receive a share, or participation, in the payments from a particular project. The payments are passed through the lessor
      to the certificate holders. The lessor typically assigns the lease and the payments to a trustee, which then distributes
      the payments to the certificate holders.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/DebtInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/DebtInstrument
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/CertificateOfParticipation
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: certificate of participation
type: Ontology Class
---

# certificate of participation

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/CertificateOfParticipation>

## Definition

debt instrument evidencing a pro rata share in a specific pledged revenue stream, usually lease payments by the issuer that are typically subject to annual appropriation

## Relationships

- **Subclass of**: [DebtInstrument](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/DebtInstrument.md)

## Annotations

- **label**: certificate of participation
- **definition**: debt instrument evidencing a pro rata share in a specific pledged revenue stream, usually lease payments by the issuer that are typically subject to annual appropriation
- **abbreviation**: COP
- **explanatoryNote**: A certificate of participation (COP) is a type of financing where an investor purchases a share of the lease revenues of a program rather than the bond being secured by those revenues. The certificate generally entitles the holder to receive a share, or participation, in the payments from a particular project. The payments are passed through the lessor to the certificate holders. The lessor typically assigns the lease and the payments to a trustee, which then distributes the payments to the certificate holders.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
